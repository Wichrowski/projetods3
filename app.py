import boto3
import os

from flask import (
    Flask,
    request,
    render_template,
    url_for,
    json,
    redirect
)
from flask_migrate import Migrate
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user
)

from models import db, Usuario
from services import (
    evento_service,
    cidade_service,
    parceiro_service
)
from filtros import Filtros

import seeding

app = Flask(__name__)

app.config.from_object("config.Config")
app.secret_key = 'secret sauce!'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db.init_app(app)

migrate = Migrate(app, db)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'form_login'


@login_manager.user_loader
def get_user(id):
    return Usuario.query.filter_by(id = int(id)).one()


@app.cli.command(help="Executa o seeding com dados de teste")
def seed():
    seeding.criar_eventos(db)


@app.route("/evento/<id_evento>")
def evento(id_evento):
    evento = evento_service.encontrar_por_id(id_evento)
    return render_template(
        "evento.html",
        evento = evento
    )


@app.route("/")
def eventos():

    filtros = Filtros(request)

    eventos = evento_service.buscar_todos()

    return render_template(
        "eventos.html",
        eventos = filtros.aplicar(eventos),
        filtros = filtros
    )


@app.route("/evento/cadastrar")
@login_required
def cadastro_evento():
    return render_template(
        "cadastrar_evento.html",
        evento = evento_service.vazio(),
        parceiro = parceiro_service
        .get_parceiro_logado(current_user),
        opcoes_cidades = cidade_service.todas()
    )


@app.route("/evento/<id_evento>/editar")
@login_required
def editar_evento(id_evento):
    return render_template(
        "cadastrar_evento.html",
        evento = evento_service.encontrar_por_id(id_evento),
        parceiro = parceiro_service
        .get_parceiro_logado(current_user),
        opcoes_cidades = cidade_service.todas()
    )


@app.route("/evento/cadastrar", methods=["POST"])
@login_required
def salvar_cadastro_evento():
    evento_service.salvar(request.form)

    return redirect(url_for('eventos'))

@app.route('/sign_s3/')
def sign_s3():
    S3_BUCKET = os.environ.get('S3_BUCKET_NAME')

    file_name = request.args.get('file_name')
    file_type = request.args.get('file_type')

    s3 = boto3.client('s3')

    presigned_post = s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key = file_name,
        Fields = {"acl": "public-read", "Content-Type": file_type},
        Conditions = [
            {"acl": "public-read"},
            {"Content-Type": file_type}
        ],
        ExpiresIn = 3600
    )

    return json.dumps({
        'data': presigned_post,
        'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
    })


@app.route("/evento/<id_evento>/deletar", methods=["POST"])
@login_required
def deletar_evento(id_evento):
    evento_service.deletar(id_evento)
    return redirect(url_for('eventos'))


@app.route('/login')
def form_login():
    return render_template('login_parceiro.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('eventos'))


@app.route('/login', methods = ['POST'])
def efetuar_login():
    apelido = request.form['apelido']
    senha = request.form['senha']

    usuario = Usuario.query.filter_by(
        apelido = apelido,
        senha = senha
    ).first()

    if usuario is None:
        return render_template('login_parceiro.html')

    login_user(usuario)
    return redirect(url_for('eventos'))


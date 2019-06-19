from flask import (
    Flask,
    request,
    render_template,
    url_for,
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
from services import evento_service, cidade_service
from filtros import Filtros

import seeding

app = Flask(__name__)

app.config.from_object("config.Config")
app.secret_key = 'secret sauce!'

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
def cadastro_evento():
    return render_template(
        "cadastrar_evento.html",
        evento = evento_service.vazio(),
        opcoes_cidades = cidade_service.todas()
    )


@app.route("/evento/<id_evento>/editar")
def editar_evento(id_evento):
    return render_template(
        "cadastrar_evento.html",
        evento = evento_service.encontrar_por_id(id_evento),
        opcoes_cidades = cidade_service.todas()
    )


@app.route("/evento/cadastrar", methods=["POST"])
def salvar_cadastro_evento():
    evento_service.salvar(request.form)
    return redirect(url_for('eventos'))


@app.route("/evento/<id_evento>/deletar", methods=["POST"])
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


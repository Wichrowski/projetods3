from flask import Flask, request, render_template, url_for, redirect
from flask_migrate import Migrate

from models import db, Evento
from services import evento_service, cidade_service

import seeding

app = Flask(__name__)

app.config.from_object("config.Config")

db.init_app(app)

migrate = Migrate(app, db)


@app.cli.command(help="Executa o seeding com dados de teste")
def seed():
    seeding.criar_eventos(db)


@app.route("/pagina-inicial")
def login_parceiro():
    return render_template("login_parceiro.html")


@app.route("/")
def eventos():
    return render_template(
        "eventos.html",
        eventos=evento_service.buscar_todos()
    )


@app.route("/meus-eventos")
def meu_eventos():
    return render_template("meus_eventos.html")


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


@app.route("/evento-especifico")
def evento_especifico():
    return render_template("evento_especifico.html")


@app.route("/evento/<id_evento>/deletar", methods=["POST"])
def deletar_evento(id_evento):
    evento_service.deletar(id_evento)
    return redirect(url_for('eventos'))

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import(
    db,
    Parceiro,
    Evento
)

import seeding

app = Flask(__name__)

app.config.from_object('config.Config')

db.init_app(app)

migrate = Migrate(app, db)

@app.cli.command(help = 'Executa o seeding com dados de teste')
def seed():
    seeding.criar_eventos(db)

@app.route("/pagina-inicial")
def login_parceiro():
    return render_template("login_parceiro.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html", eventos = Evento.query.all())

@app.route("/meus-eventos")
def meu_eventos():
    return render_template("meus_eventos.html")

@app.route("/cadastrar-evento")
def cadastro():
    return render_template("cadastrar_evento.html")

@app.route("/evento-especifico")
def evento_especifico():
    return render_template("evento_especifico.html")

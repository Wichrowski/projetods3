from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from models import(
    db,
    Parceiro,
    Evento
)

import seeding

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:projeto_ds3@localhost:5432/projeto_ds3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/seed")
def seeding():
    seeding.criar_eventos(db)

    return "ok"

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

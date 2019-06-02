from flask import Flask
from flask import render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:projeto_ds3@localhost:5432/projeto_ds3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

login_manager = LoginManager()

class Parceiro(db.Model):
    __tablename__ = 'parceiro'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(), unique = True)

class Evento(db.Model):

    __tablename__ = 'evento'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(), unique = True)
    id_parceiro = db.Column(db.Integer(), db.ForeignKey('parceiro.id'))
    parceiro = db.relationship('Parceiro')

db.create_all()

@app.route("/seed")
def seeding():
    db.session.add(
        Evento(
            nome = "Palestra de Python",
            parceiro = Parceiro(
                nome = "Python Foundation"
            )
        )
    )

    db.session.add(
        Evento(
            nome = "Palestra de Java",
            parceiro = Parceiro(
                nome = "Oracle"
            )
        )
    )

    db.session.add(
        Evento(
            nome = "Workshop de Rails",
            parceiro = Parceiro(
                nome = "Plataformatec"
            )
        )
    )

    db.session.commit()

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

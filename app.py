from flask import Flask
from flask import render_template
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()

class Evento:
    def __init__(self, nome, nome_parceiro):
        self.nome = nome
        self.nome_parceiro = nome_parceiro

@app.route("/pagina-inicial")
def login_parceiro():
    return render_template("login_parceiro.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html", eventos = [
        Evento("Palestra de Python", "Python Foundation"),
        Evento("Palestra de Java", "Oracle"),
        Evento("Workshop de Rails", "Plataformatec")
    ])

@app.route("/meus-eventos")
def meu_eventos():
    return render_template("meus_eventos.html")

@app.route("/cadastrar-evento")
def cadastro():
    return render_template("cadastrar_evento.html")

@app.route("/evento-especifico")
def evento_especifico():
    return render_template("evento_especifico.html")

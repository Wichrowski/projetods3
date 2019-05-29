from flask import Flask
from flask import render_template
from flask_login import LoginManager
app = Flask(__name__)
login_manager = LoginManager()

@app.route("/pagina-inicial")
def login_parceiro():
    return render_template("login_parceiro.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html")
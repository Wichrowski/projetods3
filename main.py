from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def login_parceiro():
    return render_template("login_parceiro.html")
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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


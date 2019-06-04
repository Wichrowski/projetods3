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
    parceiro = db.relationship('Parceiro')
    data = db.Column(db.Date())
    tipo = db.Column(db.Enum(
        'Workshop',
        'Palestra',
        'Curso',
        'Congresso',
        name = 'tipo_evento'))

    area = db.Column(db.Enum(
        'Informática',
        'Medicina',
        'Química',
        'Administração',
        name = 'area_evento'))

    id_parceiro = db.Column(db.Integer(), db.ForeignKey('parceiro.id'))

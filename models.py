import enum
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Estado(db.Model):

    __tablename__ = 'estado'

    codigo = db.Column(db.String(), primary_key = True)
    nome = db.Column(db.String())


class Cidade(db.Model):

    __tablename__ = 'cidade'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String())
    estado = db.relationship('Estado')

    codigo_estado = db.Column(
        db.String(),
        db.ForeignKey('estado.codigo')
    )


class Endereco(db.Model):

    __tablename__ = 'endereco'

    id = db.Column(db.Integer(), primary_key = True)
    logradouro = db.Column(db.String())

    cidade = db.relationship('Cidade')

    id_cidade = db.Column(
        db.Integer(),
        db.ForeignKey('cidade.id')
    )


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer(), primary_key = True)
    apelido = db.Column(db.String(), unique = True)
    senha = db.Column(db.String(), unique = True)


class Parceiro(db.Model):

    __tablename__ = 'parceiro'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(), unique = True)

    usuario = db.relationship('Usuario')

    id_usuario = db.Column(
        db.Integer(),
        db.ForeignKey('usuario.id')
    )


def valores_enum(enum_alvo):
    return [
        member.value
        for name, member
        in enum_alvo.__members__.items()
    ]


class TipoEvento(enum.Enum):

    WORKSHOP = 'Workshop'
    PALESTRA = 'Palestra'
    CURSO = 'Curso'
    CONGRESSO = 'Congresso'
    MEETUP = 'Meetup'


class AreaEvento(enum.Enum):

    ADMINISTRACAO = 'Administração'
    ARQUITETURA = 'Arquitetura'
    ARTE = 'Arte'
    CIENCIAS_SOCIAIS = 'Ciências Sociais'
    COMUNICACAO = 'Comunicação'
    DESIGN = 'Design'
    DIREITO = 'Direito'
    ECONOMIA = 'Economia'
    EDUCACAO = 'Educação'
    ENGENHARIA = 'Engenharia'
    GASTRONOMIA = 'Gastronomia'
    INFORMATICA = 'Informática'
    NEGOCIOS = 'Negócios'
    SAUDE = 'Saúde'
    QUIMICA = 'Química'
    TURISMO = 'Turismo'


class Evento(db.Model):

    __tablename__ = 'evento'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(), unique = True)
    data = db.Column(db.Date())
    descricao = db.Column(db.String(), nullable = True)
    url_imagem = db.Column(db.String(), nullable = True)

    tipo = db.Column(db.Enum(*valores_enum(TipoEvento), name = 'tipo_evento'))
    area = db.Column(db.Enum(*valores_enum(AreaEvento), name = 'area_evento'))

    parceiro = db.relationship('Parceiro')
    endereco = db.relationship('Endereco')

    id_parceiro = db.Column(
        db.Integer(),
        db.ForeignKey('parceiro.id')
    )

    id_endereco = db.Column(
        db.Integer(),
        db.ForeignKey('endereco.id')
    )



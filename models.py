from flask_sqlalchemy import SQLAlchemy

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


class Parceiro(db.Model):

    __tablename__ = 'parceiro'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(), unique = True)


class Evento(db.Model):

    __tablename__ = 'evento'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(), unique = True)
    data = db.Column(db.Date())
    tipo = db.Column(db.Enum(
        'Workshop',
        'Palestra',
        'Curso',
        'Congresso',
        name = 'tipo_evento')
    )

    area = db.Column(db.Enum(
        'Administração',
        'Arquitetura',
        'Arte',
        'Ciências Sociais',
        'Comunicação',
        'Design',
        'Direito',
        'Economia',
        'Educação',
        'Engenharia',
        'Gastronomia',
        'Informática',
        'Negócios',
        'Saúde',
        'Química',
        'Turismo',
        name = 'area_evento')
    )

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

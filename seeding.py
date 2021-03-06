from datetime import datetime
from models import (
    Cidade,
    Evento,
    Estado,
    Endereco,
    Parceiro,
    Usuario
)


def data(valor_em_string):
    return datetime.strptime(valor_em_string, '%d/%m/%Y')


def estado(codigo):
    return Estado.query.filter_by(codigo = codigo).one()


def cidade(nome):
    return Cidade.query.filter_by(nome = nome).one()


def criar_eventos(db):
    Evento.query.delete()
    Parceiro.query.delete()
    Usuario.query.delete()
    Endereco.query.delete()
    Cidade.query.delete()
    Estado.query.delete()

    db.session.add(
        Estado(
            codigo = "CE",
            nome = "Ceará"
        )
    )

    db.session.add(
        Estado(
            codigo = "RS",
            nome = "Rio Grande do Sul"
        )
    )

    db.session.add(
        Estado(
            codigo = "PR",
            nome = "Paraná"
        )
    )

    db.session.add(
        Estado(
            codigo = "SP",
            nome = "São Paulo"
        )
    )

    db.session.commit()

    db.session.add(
        Cidade(
            estado = estado("RS"),
            nome = "Porto Alegre"
        )
    )

    db.session.add(
        Cidade(
            estado = estado("PR"),
            nome = "Curitiba"
        )
    )

    db.session.add(
        Cidade(
            estado = estado("CE"),
            nome = "Fortaleza"
        )
    )

    db.session.add(
        Cidade(
            estado = estado("SP"),
            nome = "São Paulo"
        )
    )

    db.session.commit()

    db.session.add(
        Evento(
            nome = "Palestra de Python",
            tipo = 'Palestra',
            area = 'Informática',
            data = data('04/06/2019'),
            parceiro = Parceiro(
                nome = "Python Foundation",
                usuario = Usuario(
                    apelido = 'py_foundation',
                    senha = 'py_foundation'
                )
            ),
            endereco = Endereco(
                cidade = cidade("Porto Alegre"),
                logradouro = "Avenida Carlos Gomes, 500"
            ),
            descricao = 'Palestra de python',
            url_imagem = '/static/placeholder.png'
        )
    )

    db.session.add(
        Evento(
            nome = "Palestra de Java",
            tipo = 'Palestra',
            area = 'Informática',
            data = data('04/07/2019'),
            parceiro = Parceiro(
                nome = "Oracle",
                usuario = Usuario(
                    apelido = 'oracle',
                    senha = 'oracle'
                )
            ),
            endereco = Endereco(
                cidade = cidade("Curitiba"),
                logradouro = "Av. Pres. Getúlio Vargas, 635"
            ),
            descricao = 'Palestra de Java',
            url_imagem = '/static/placeholder.png'
        )
    )

    db.session.add(
        Evento(
            nome = "Workshop de Rails",
            tipo = 'Workshop',
            area = 'Informática',
            data = data('05/08/2019'),
            parceiro = Parceiro(
                nome = "Plataformatec",
                usuario = Usuario(
                    apelido = 'plataformatec',
                    senha = 'plataformatec'
                )
            ),
            endereco = Endereco(
                cidade = cidade("Curitiba"),
                logradouro = "Avenida Doutor Silas Munguba, 1700"
            ),
            descricao = 'Como desenvolver uma aplicação Web com Ruby on Rails',
            url_imagem = '/static/placeholder.png'
        )
    )

    db.session.add(
        Evento(
            nome = "Testes funcionais com Cypress",
            parceiro = Parceiro(
                nome = "Alura",
                usuario = Usuario(
                    apelido = 'alura',
                    senha = 'alura'
                )
            ),
            tipo = 'Curso',
            area = 'Informática',
            data = data('04/08/2019'),
            endereco = Endereco(
                cidade = cidade("São Paulo"),
                logradouro = "Avenida Paulista, 1050"
            ),
            descricao = 'Como automatizar o teste de aplicações com Cypress',
            url_imagem = '/static/placeholder.png'
        )
    )

    db.session.add(
        Evento(
            nome = "Congresso Nacional de Ácido Sulfúrico",
            tipo = 'Congresso',
            area = 'Química',
            data = data('10/09/2019'),
            parceiro = Parceiro(
                nome = "Instituto Nacional de Química",
                usuario = Usuario(
                    apelido = 'instituto_quimica',
                    senha = 'instituto_quimica'
                )
            ),
            endereco = Endereco(
                cidade = cidade("Porto Alegre"),
                logradouro = "Avenida Diário de Notícias, 1000"
            ),
            descricao = 'Congresso sobre Ácido Sulfúrico',
            url_imagem = '/static/placeholder.png'
        )
    )

    db.session.add(
        Evento(
            nome = "Curso de massas",
            tipo = 'Curso',
            area = 'Gastronomia',
            data = data('10/10/2019'),
            parceiro = Parceiro(
                nome = "Alho e Oleo Gastronomia",
                usuario = Usuario(
                    apelido = 'alho_oleo',
                    senha = 'alho_oleo'
                )
            ),
            endereco = Endereco(
                cidade = cidade("Porto Alegre"),
                logradouro = "Avenida Diário de Notícias, 1000"
            ),
            descricao = 'Aprenda sobre diferentes tipos de massa na prática,' +
            ' criando três opções de jantar. ',
            url_imagem = '/static/placeholder.png'

        )
    )

    db.session.add(
        Evento(
            nome = "Meetup Node.js",
            tipo = 'Meetup',
            area = 'Informática',
            data = data('10/11/2019'),
            parceiro = Parceiro(
                nome = "DbServer",
                usuario = Usuario(
                    apelido = 'db_server',
                    senha = 'db_server'
                )
            ),
            endereco = Endereco(
                cidade = cidade("Porto Alegre"),
                logradouro = "Avenida Ipiranga, 6681, 99A"
            ),
            descricao = 'Evento para falar sobre Node.js',
            url_imagem = '/static/placeholder.png'
        )
    )

    db.session.commit()

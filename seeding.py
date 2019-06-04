from datetime import datetime
from models import (
    Evento,
    Parceiro
)


def data(valor_em_string):
    return datetime.strptime(valor_em_string, '%d/%m/%Y')


def criar_eventos(db):
    Evento.query.delete()
    Parceiro.query.delete()

    db.session.add(
        Evento(
            nome = "Palestra de Python",
            parceiro = Parceiro(
                nome = "Python Foundation"
            ),
            tipo = 'Palestra',
            area = 'Informática',
            data = data('04/06/2019')
        )
    )

    db.session.add(
        Evento(
            nome = "Palestra de Java",
            parceiro = Parceiro(
                nome = "Oracle"
            ),
            tipo = 'Palestra',
            area = 'Informática',
            data = data('04/07/2019')
        )
    )

    db.session.add(
        Evento(
            nome = "Workshop de Rails",
            parceiro = Parceiro(
                nome = "Plataformatec"
            ),
            tipo = 'Workshop',
            area = 'Informática',
            data = data('05/08/2019')
        )
    )

    db.session.add(
        Evento(
            nome = "Testes funcionais com Cypress",
            parceiro = Parceiro(
                nome = "Alura"
            ),
            tipo = 'Curso',
            area = 'Informática',
            data = data('04/08/2019')
        )
    )

    db.session.add(
        Evento(
            nome = "Congresso Nacional de Ácido Sulfúrico",
            parceiro = Parceiro(
                nome = "Instituto Nacional de Química"
            ),
            tipo = 'Congresso',
            area = 'Química',
            data = data('10/09/2019')
        )
    )

    db.session.commit()

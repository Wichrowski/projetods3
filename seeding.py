from models import(
    Evento,
    Parceiro
)

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
            area = 'Informática'
        )
    )

    db.session.add(
        Evento(
            nome = "Palestra de Java",
            parceiro = Parceiro(
                nome = "Oracle"
            ),
            tipo = 'Palestra',
            area = 'Informática'
        )
    )

    db.session.add(
        Evento(
            nome = "Workshop de Rails",
            parceiro = Parceiro(
                nome = "Plataformatec"
            ),
            tipo = 'Workshop',
            area = 'Informática'
        )
    )

    db.session.add(
        Evento(
            nome = "Testes funcionais com Cypress",
            parceiro = Parceiro(
                nome = "Alura"
            ),
            tipo = 'Curso',
            area = 'Informática'
        )
    )

    db.session.add(
        Evento(
            nome = "Congresso Nacional de Ácido Sulfúrico",
            parceiro = Parceiro(
                nome = "Instituto Nacional de Química"
            ),
            tipo = 'Congresso',
            area = 'Química'
        )
    )

    db.session.commit()

from models import(
    Evento,
    Parceiro
)

def criar_eventos(db):
    db.session.add(
        Evento(
            nome = "Palestra de Python",
            parceiro = Parceiro(
                nome = "Python Foundation"
            ),
            tipo = 'Palestra'
        )
    )

    db.session.add(
        Evento(
            nome = "Palestra de Java",
            parceiro = Parceiro(
                nome = "Oracle"
            ),
            tipo = 'Palestra'
        )
    )

    db.session.add(
        Evento(
            nome = "Workshop de Rails",
            parceiro = Parceiro(
                nome = "Plataformatec"
            ),
            tipo = 'Workshop'
        )
    )

    db.session.add(
        Evento(
            nome = "Testes funcionais com Cypress",
            parceiro = Parceiro(
                nome = "Alura"
            ),
            tipo = 'Curso'
        )
    )

    db.session.commit()

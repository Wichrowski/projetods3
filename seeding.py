def criar_eventos(db):
    db.session.add(
        Evento(
            nome = "Palestra de Python",
            parceiro = Parceiro(
                nome = "Python Foundation"
            )
        )
    )

    db.session.add(
        Evento(
            nome = "Palestra de Java",
            parceiro = Parceiro(
                nome = "Oracle"
            )
        )
    )

    db.session.add(
        Evento(
            nome = "Workshop de Rails",
            parceiro = Parceiro(
                nome = "Plataformatec"
            )
        )
    )

    db.session.commit()

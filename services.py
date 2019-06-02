from models import db, Evento


class EventoService:
    def buscar_todos(self):
        return Evento.query.all()

    def salvar(self, form):
        novo_evento = Evento(
            nome=form['nome'],
            area=form['area'],
            tipo=form['tipo']
        )

        db.session.add(novo_evento)
        db.session.commit()


evento_service = EventoService()

from models import db, Evento
from datetime import datetime


def interpretar_data_form(form):
    return datetime.strptime(form['data'], '%d/%m/%Y').date()


class EventoService:
    def buscar_todos(self):
        return Evento.query.all()

    def deletar(self, id_evento):
        Evento.query.filter_by(id = id_evento).delete()
        db.session.commit()

    def salvar(self, form):
        novo_evento = Evento(
            nome = form['nome'],
            area = form['area'],
            tipo = form['tipo'],
            data = interpretar_data_form(form)
        )

        db.session.add(novo_evento)
        db.session.commit()


evento_service = EventoService()

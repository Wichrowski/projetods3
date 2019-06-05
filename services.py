from models import db, Evento, Cidade, Endereco
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
            data = interpretar_data_form(form),
            endereco = Endereco(
                id_cidade = form['id_cidade']
            )
        )

        db.session.add(novo_evento)
        db.session.commit()


class CidadeService:
    def todas(self):
        return Cidade.query.all()


cidade_service = CidadeService()
evento_service = EventoService()

from models import (
    db,
    TipoEvento,
    AreaEvento,
    Evento,
    Cidade,
    Endereco,
    Parceiro,
    valores_enum
)
from datetime import datetime


def interpretar_data_form(form):
    return datetime.strptime(form['data'], '%d/%m/%Y').date()


class EventoService:

    def vazio(self):
        return Evento(
            nome = "",
            descricao = "",
            data = datetime.today().strftime('%d/%m/%Y'),
            endereco = Endereco()
        )

    def areas_de_evento(self):
        return valores_enum(AreaEvento)

    def tipos_de_evento(self):
        return valores_enum(TipoEvento)

    def encontrar_por_id(self, id):
        return Evento.query.filter_by(id = id).one()

    def buscar_todos(self):
        return Evento.query.all()

    def buscar_por(self, filtros):
        return Evento.query.filter_by(**filtros).all()

    def deletar(self, id_evento):
        Evento.query.filter_by(id = id_evento).delete()
        db.session.commit()

    def salvar(self, form):
        if form['id'] != 'None':
            evento = Evento\
                .query\
                .filter_by(id = form['id']).one()

            evento.nome = form['nome']
            evento.area = form['area']
            evento.tipo = form['tipo']
            evento.descricao = form['descricao']
            evento.data = interpretar_data_form(form)
            evento.endereco.id_cidade = form['id_cidade']
            evento.id_parceiro = form['id_parceiro']
            evento.url_imagem = form['url_imagem']
            db.session.commit()
        else:
            novo_evento = Evento(
                nome = form['nome'],
                area = form['area'],
                tipo = form['tipo'],
                descricao = form['descricao'],
                url_imagem = form['url_imagem'],
                data = interpretar_data_form(form),
                endereco = Endereco(
                    id_cidade = form['id_cidade']
                ),
                id_parceiro = form['id_parceiro']
            )

            db.session.add(novo_evento)
            db.session.commit()


class CidadeService:
    def todas(self):
        return Cidade.query.all()


class ParceiroService:
    def get_parceiro_logado(self, current_user):
        return Parceiro.query.filter_by(
            id_usuario = current_user.id
        ).one()


cidade_service = CidadeService()
evento_service = EventoService()
parceiro_service = ParceiroService()

from models import TipoEvento, AreaEvento, Cidade, Parceiro


class Filtros:

    def __init__(self, request):
        self.request = request
        pass

    def filtros_ativos(self):
        return dict(
            filter(self._filtro_ausente, [
                self._parametro_de_filtro('tipo_de_evento'),
                self._parametro_de_filtro('area_de_evento'),
                self._parametro_de_filtro('cidade'),
                self._parametro_de_filtro('parceiro')
            ])
        )

    def tipos_de_evento(self):
        return [
            OpcaoDeFiltro(member.value, member.value)
            for name, member
            in TipoEvento.__members__.items()
        ]

    def areas_de_evento(self):
        return [
            OpcaoDeFiltro(member.value, member.value)
            for name, member
            in AreaEvento.__members__.items()
        ]

    def cidades(self):
        return [
            OpcaoDeFiltro(cidade.nome, str(cidade.id))
            for cidade in Cidade.query.all()
        ]

    def parceiros(self):
        return [
            OpcaoDeFiltro(parceiro.nome, str(parceiro.id))
            for parceiro in Parceiro.query.all()
        ]

    def aplicar(self, eventos):
        return [
            evento
            for evento
            in eventos
            if self._match_tipo(evento)
            and self._match_area(evento)
            and self._match_cidade(evento)
            and self._match_parceiro(evento)
        ]

    def _match_tipo(self, evento):
        if self.filtros_ativos().get('tipo_de_evento') is None:
            return True

        return evento.tipo == self.filtros_ativos().get('tipo_de_evento')

    def _match_area(self, evento):
        if self.filtros_ativos().get('area_de_evento') is None:
            return True

        return evento.area == self.filtros_ativos().get('area_de_evento')

    def _match_cidade(self, evento):
        if self.filtros_ativos().get('cidade') is None:
            return True

        return evento.endereco.cidade.id == int(self.filtros_ativos().get('cidade'))

    def _match_parceiro(self, evento):
        if self.filtros_ativos().get('parceiro') is None:
            return True

        return evento.parceiro.id == int(self.filtros_ativos().get('parceiro'))

    def _parametro_de_filtro(self, nome):
        return (nome, self.request.args.get(nome))

    def _filtro_ausente(self, param_tuple):
        return param_tuple[1] is not None and param_tuple[1] != ''


class OpcaoDeFiltro:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

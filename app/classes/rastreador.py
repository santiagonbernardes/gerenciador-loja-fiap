from datetime import date

from app.classes.persistente import Persistente
from app.classes.produto import Produto
from app.classes.repositorio import Repositorio


class Rastreador:
    def __init__(self, repositorio: Repositorio) -> None:
        self.repositorio: Repositorio[Evento] = repositorio

    def rastreie(self, estoque, produto: Produto, nome_evento: str, quantidade_entrada: int,
                 quantidade_original: int) -> None:
        evento = Evento(estoque, produto, nome_evento, quantidade_entrada, quantidade_original)
        self.repositorio.adicionar(evento)


class Evento(Persistente):
    def __init__(self, estoque, produto: Produto, evento: str, quantidade_entrada: int,
                 quantidade_original: int) -> None:
        super().__init__()
        self.evento: str = evento
        self.data: date = date.today()
        self.codigo_produto = produto.codigo
        self.quantidade_original = quantidade_original
        self.quantidade_entrada = quantidade_entrada
        self.quantidade_atualizada = estoque.obtenha_quantidade_estocada(produto)

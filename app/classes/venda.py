from datetime import date

from app.classes.persistente import Persistente
from app.classes.produto import Produto


class Venda(Persistente):

    def __init__(self) -> None:
        super().__init__()
        self.data: date = date.today()
        self.itens: list[ItemVenda] = []

    def adicione_item(self, produto: Produto, quantidade: int) -> None:
        for item_venda in self.itens:
            if item_venda.codigo_produto == produto.codigo:
                item_venda.quantidade += quantidade
                return

        item_venda = ItemVenda(produto, quantidade)
        self.itens.append(item_venda)


class ItemVenda:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.codigo_produto: int = produto.codigo
        self.quantidade: int = quantidade
        self.valor_unitario: float = produto.preco

    def calcule_valor_total(self) -> float:
        return self.quantidade * self.valor_unitario

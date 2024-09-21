from datetime import date

from app.classes.cupom import Cupom
from app.classes.persistente import Persistente
from app.classes.produto import Produto


class Venda(Persistente):

    def __init__(self) -> None:
        super().__init__()
        self.data: date = date.today()
        self.itens: list[ItemVenda] = []
        self.cupom: Cupom | None = None

    def adicione_item(self, produto: Produto, quantidade: int) -> None:
        for item_venda in self.itens:
            if item_venda.codigo_produto == produto.codigo:
                item_venda.quantidade += quantidade
                return

        item_venda = ItemVenda(produto, quantidade)
        self.itens.append(item_venda)

    def calcule_subtotal(self) -> float:
        subtotal: float = 0.0
        for item_venda in self.itens:
            subtotal += item_venda.calcule_valor_total()
        return subtotal

    def calcule_valor_total(self) -> float:
        if not self.cupom:
            return self.calcule_subtotal()

        subtotal: float = self.calcule_subtotal()
        return subtotal - (subtotal * self.cupom.porcentagem_desconto / 100)


class ItemVenda:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.codigo_produto: int = produto.codigo
        self.quantidade: int = quantidade
        self.valor_unitario: float = produto.preco

    def calcule_valor_total(self) -> float:
        return self.quantidade * self.valor_unitario

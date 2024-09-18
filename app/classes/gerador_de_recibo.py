from app.classes.produto import Produto
from app.classes.repositorio import Repositorio
from app.classes.venda import Venda


class GeradorDeRecibo:
    def __init__(self, venda: Venda, repositorio_de_produtos: Repositorio[Produto]) -> None:
        self.venda: Venda = venda
        self.repositorio_de_produtos: Repositorio[Produto] = repositorio_de_produtos

    def gerar_recibo(self) -> str:
        return f""""
        Recibo da venda #{self.venda.codigo}.
        Data da Venda: {self.venda.data}.
        Itens:
        {self.gere_itens()}
        Valor Total da Venda: R${self.venda.calcule_valor_total()}.
        """

    def gere_itens(self) -> str:
        items = ''
        for item_venda in self.venda.itens:
            produto = self.repositorio_de_produtos.obtenha(item_venda.codigo_produto)
            items += (f'#{produto.codigo}: {produto.nome} - Quantidade: {item_venda.quantidade} - '
                      f'Valor Unitário: R$ {item_venda.valor_unitario} - '
                      f'Valor Total: R$ {item_venda.calcule_valor_total()}\n')

        return items

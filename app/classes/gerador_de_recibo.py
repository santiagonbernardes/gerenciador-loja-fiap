from tabulate import tabulate

from app.classes.produto import Produto
from app.classes.repositorio import Repositorio
from app.classes.venda import Venda


class GeradorDeRecibo:
    def __init__(self, venda: Venda, repositorio_de_produtos: Repositorio[Produto]) -> None:
        self.venda: Venda = venda
        self.repositorio_de_produtos: Repositorio[Produto] = repositorio_de_produtos
        self.headers_recibo: list[str] = ['Recibo da Venda #', 'Data da Venda']
        self.headers_itens: list[str] = ['Código', 'Nome', 'Quantidade', 'Valor Unitário', 'Valor Total']

    def gerar_recibo(self) -> str:
        cabecalho = tabulate([[self.venda.codigo, self.venda.data]], headers=self.headers_recibo, tablefmt='grid')
        itens = self.gere_itens()
        rodape = tabulate([[self.venda.calcule_valor_total()]], headers=['Valor Total da Venda'], tablefmt='grid')
        return f'{cabecalho}{itens}{rodape}'

    def gere_itens(self) -> str:
        dados_itens = []

        for item_venda in self.venda.itens:
            produto = self.repositorio_de_produtos.obtenha(item_venda.codigo_produto)
            dados = [
                produto.codigo,
                produto.nome,
                item_venda.quantidade,
                item_venda.valor_unitario,
                item_venda.calcule_valor_total()
            ]
            dados_itens.append(dados)

        return tabulate(dados_itens, headers=self.headers_itens, tablefmt='pretty')

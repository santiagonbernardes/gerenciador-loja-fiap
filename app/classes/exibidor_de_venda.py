from tabulate import tabulate

from app.classes.produto import Produto
from app.classes.repositorio import Repositorio
from app.classes.venda import Venda


class ExibidorDeVenda:
    def __init__(self, venda: Venda, repositorio_de_produtos: Repositorio[Produto]) -> None:
        self.venda: Venda = venda
        self.repositorio_de_produtos: Repositorio[Produto] = repositorio_de_produtos
        self.headers_recibo: list[str] = ['Código da Venda #', 'Data da Venda']
        self.headers_itens: list[str] = ['Código', 'Nome', 'Quantidade', 'Valor Unitário', 'Valor Total']
        self.headers_rodape = ['Subtotal', 'Cupom Aplicado', '% de desconto', 'Valor Total da Venda']

    def exiba_todos(self) -> str:
        if self.venda.cupom:
            nome_cupom = self.venda.cupom.nome
            porcentagem_desconto = self.venda.cupom.porcentagem_desconto
        else:
            nome_cupom = 'Sem cupom'
            porcentagem_desconto = 0

        dados_cabecalho = [self.venda.codigo, self.venda.data]
        dados_rodape = [self.venda.calcule_subtotal(), nome_cupom, f'{porcentagem_desconto}%',
                        f'R${self.venda.calcule_valor_total()}']

        cabecalho = tabulate([dados_cabecalho], headers=self.headers_recibo, tablefmt='grid')
        itens = self.gere_itens()
        rodape = tabulate([dados_rodape], headers=self.headers_rodape, tablefmt='grid')
        return f'{cabecalho}{itens}{rodape}'

    def gere_itens(self) -> str:
        dados_itens = []

        for item_venda in self.venda.itens:
            produto = self.repositorio_de_produtos.obtenha(item_venda.codigo_produto)
            dados = [
                produto.codigo,
                produto.nome,
                item_venda.quantidade,
                f'R${item_venda.valor_unitario}',
                f'R${item_venda.calcule_valor_total()}'
            ]
            dados_itens.append(dados)

        return tabulate(dados_itens, headers=self.headers_itens, tablefmt='pretty')

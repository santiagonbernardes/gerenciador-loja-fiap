from tabulate import tabulate

from app.classes.estoque import Estoque
from app.classes.produto import Produto
from app.classes.repositorio import Repositorio
from app.excecoes import NaoHaProdutosException


class ExibidorDeProdutos:
    def __init__(self, repositorio: Repositorio, estoque: Estoque) -> None:
        self.repositorio: Repositorio = repositorio
        self.estoque: Estoque = estoque
        self.headers: list[str] = ['Código', 'Nome', 'Quantidade em estoque', 'Preço']

    def exiba_todos(self) -> None:
        produtos: list[Produto] = self.repositorio.listar()

        if len(produtos) == 0:
            raise NaoHaProdutosException()

        dados_produtos = []

        for produto in produtos:
            dados = [produto.codigo, produto.nome, self.estoque.obtenha_quantidade_estocada(produto),
                     f'R${produto.preco}']
            dados_produtos.append(dados)

        print('Produtos disponíveis:\n')
        print(tabulate(dados_produtos, headers=self.headers, tablefmt='pretty'))

from app.classes.estoque import Estoque
from app.classes.produto import Produto
from app.classes.repositorio import Repositorio
from app.excecoes import NaoHaProdutosException


class ExibidorDeProdutos:
    def __init__(self, repositorio: Repositorio, estoque: Estoque) -> None:
        self.repositorio: Repositorio = repositorio
        self.estoque: Estoque = estoque

    def exiba_todos(self) -> None:
        produtos: list[Produto] = self.repositorio.listar()

        if len(produtos) == 0:
            raise NaoHaProdutosException()

        print('Produtos disponíveis:\n')
        print('Código - Nome - Quantidade em estoque - Preço\n')

        for produto in produtos:
            print(f'{produto.codigo} - {produto.nome} - '
                  f'{self.estoque.obtenha_quantidade_estocada(produto)} - R$ {produto.preco}')

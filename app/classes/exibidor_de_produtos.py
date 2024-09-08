from app.excecoes import NaoHaProdutosException


class ExibidorDeProdutos:
    def __init__(self, repositorio, estoque):
        self.repositorio = repositorio
        self.estoque = estoque

    def exiba_todos(self):
        produtos = self.repositorio.listar()

        if len(produtos) == 0:
            raise NaoHaProdutosException()

        print('Produtos disponíveis:\n')
        print('Código - Nome - Quantidade em estoque\n')

        for produto in produtos:
            print(f'{produto.codigo} - {produto.nome} - {self.estoque.obtenha_quantidade_estocada(produto)}')

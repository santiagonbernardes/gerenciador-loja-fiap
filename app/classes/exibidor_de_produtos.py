from app.excecoes import NaoHaProdutosException


class ExibidorDeProdutos:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def exiba_todos(self):
        produtos = self.repositorio.listar()

        if len(produtos) == 0:
            raise NaoHaProdutosException()

        for produto in produtos:
            print(f'{produto.codigo} - {produto.nome}')

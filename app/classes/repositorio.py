from app.classes.gerador_de_codigo import GeradorDeCodigo
from app.classes.produto import Produto


class Repositorio:
    def __init__(self, gerador_de_codigo: GeradorDeCodigo) -> None:
        self.gerador_de_codigo = gerador_de_codigo

    def adicionar(self, produto: Produto) -> None:
        produto.codigo = self.gerador_de_codigo.gerar()
        self.salve(produto)

    def obtenha(self, codigo) -> Produto:
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')

    def listar(self) -> list[Produto]:
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')

    # Daqui pra baixo, tudo deveria ser privado ou protegido
    def salve(self, produto) -> None:
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')


class RepositorioEmMemoria(Repositorio):
    def __init__(self, gerador_de_codigo: GeradorDeCodigo) -> None:
        super().__init__(gerador_de_codigo)
        self.produtos: list[Produto] = []

    def obtenha(self, codigo) -> Produto | None:
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def listar(self) -> list[Produto]:
        return self.produtos

    def salve(self, produto) -> None:
        self.produtos.append(produto)

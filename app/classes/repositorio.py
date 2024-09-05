class Repositorio:
    def __init__(self, gerador_de_codigo):
        self.gerador_de_codigo = gerador_de_codigo

    def adicionar(self, produto):
        produto.codigo = self.gerador_de_codigo.gerar()
        self.salve(produto)

    def obtenha(self, codigo):
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')

    def listar(self):
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')

    # Daqui pra baixo, tudo deveria ser privado ou protegido
    def salve(self, produto):
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')


class RepositorioEmMemoria(Repositorio):
    def __init__(self, gerador_de_codigo):
        super().__init__(gerador_de_codigo)
        self.produtos = []

    def obtenha(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def listar(self):
        return self.produtos

    def salve(self, produto):
        self.produtos.append(produto)

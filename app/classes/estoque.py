from app.excecoes import ProdutoSemEstoqueException, RemocaoMaiorQueEstoqueException, ProdutoNaoEstocadoException


class Estoque:

    def __init__(self, limite_estoque_baixo=3):
        self.produtos_estocados = {}
        self.limite_estoque_baixo = limite_estoque_baixo

    def adicionar(self, produto, quantidade):
        self.execute_observando_limite_estoque_baixo(self.execute_adicionar, produto, quantidade)

    def remover(self, produto, quantidade_remover):
        self.execute_observando_limite_estoque_baixo(self.execute_remover, produto, quantidade_remover)

    def atualizar(self, produto, nova_quantidade):
        self.execute_observando_limite_estoque_baixo(self.execute_atualizar, produto, nova_quantidade)

    def obtenha_quantidade_estocada(self, produto):
        if produto.codigo not in self.produtos_estocados:
            raise ProdutoNaoEstocadoException()
        return self.produtos_estocados[produto.codigo]

    def atualize_limite_estoque_baixo(self, novo_limite):
        self.limite_estoque_baixo = novo_limite
        for codigo_produto, quantidade in self.produtos_estocados.items():
            if quantidade < novo_limite:
                self.mostre_mensagem_estoque_baixo(codigo_produto)

    # Daqui pra baixo, tudo deveria ser privado

    def execute_observando_limite_estoque_baixo(self, funcao, *args):
        # Esta funcão executará a função passada como parâmetro e verificará se o estoque está baixo para notificar
        # o usuário. O único requisito é que o primeiro parâmetro da função a ser executada seja o produto.
        funcao(*args)
        produto = args[0]  # Produto tem que ser o primeiro parâmetro
        codigo_produto = produto.codigo
        if self.produtos_estocados[codigo_produto] < self.limite_estoque_baixo:
            self.mostre_mensagem_estoque_baixo(codigo_produto)

    def execute_adicionar(self, produto, quantidade):
        codigo_produto = produto.codigo
        if codigo_produto in self.produtos_estocados:
            self.produtos_estocados[codigo_produto] += quantidade
        else:
            self.execute_atualizar(produto, quantidade)

    def execute_remover(self, produto, quantidade_remover):
        codigo_produto = produto.codigo

        if codigo_produto not in self.produtos_estocados:
            raise ProdutoSemEstoqueException()

        if quantidade_remover > self.produtos_estocados[codigo_produto]:
            raise RemocaoMaiorQueEstoqueException()

        self.produtos_estocados[codigo_produto] -= quantidade_remover

    def execute_atualizar(self, produto, nova_quantidade):
        codigo_produto = produto.codigo
        self.produtos_estocados[codigo_produto] = nova_quantidade

    def mostre_mensagem_estoque_baixo(self, codigo_produto):
        estoque_atual = self.produtos_estocados[codigo_produto]
        print(f'Atenção: o produto#{codigo_produto} está com estoque baixo. Estoque atual é: {estoque_atual}.')

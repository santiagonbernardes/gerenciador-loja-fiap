from app.excecoes import ProdutoSemEstoqueException, RemocaoMaiorQueEstoqueException


class Estoque:
    def __init__(self, limite_estoque_baixo=3):
        self.produtos_estocados = {}
        self.limite_estoque_baixo = limite_estoque_baixo

    def adicionar(self, produto, quantidade):
        codigo_produto = produto.codigo
        if codigo_produto in self.produtos_estocados:
            self.produtos_estocados[codigo_produto] += quantidade
        else:
            self.atualizar(produto, quantidade)

    def quantidade_estocada(self, produto):
        return self.produtos_estocados.get(produto.codigo, 0)

    def remover(self, produto, quantidade_remover):
        codigo_produto = produto.codigo

        if codigo_produto not in self.produtos_estocados:
            raise ProdutoSemEstoqueException()

        if quantidade_remover > self.produtos_estocados[codigo_produto]:
            raise RemocaoMaiorQueEstoqueException()

        self.produtos_estocados[codigo_produto] -= quantidade_remover

        # TODO: mensagem de estoque baixo para outro lugar? yield?
        if self.produtos_estocados[codigo_produto] < self.limite_estoque_baixo:
            print(f'Atenção: o produto#{codigo_produto} está com estoque baixo.')

    def atualizar(self, produto, nova_quantidade):
        codigo_produto = produto.codigo
        self.produtos_estocados[codigo_produto] = nova_quantidade
        if self.produtos_estocados[codigo_produto] < self.limite_estoque_baixo:
            print(f'Atenção: o produto#{codigo_produto} está com estoque menor que {self.limite_estoque_baixo}.')

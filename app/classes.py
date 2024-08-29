class Produto:

    def __init__(self, nome, categoria, preco, descricao, fornecedor):
        # TODO: código vai ser definido por outra classe
        # TODO: quantidade vai ser definida no estoque
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.codigo = None


class Repositorio:
    # Esta classe pode ser generalizada para aceitar qualquer tipo de objeto
    def __init__(self, gerador_de_codigo):
        self.produtos = []
        self.gerador_de_codigo = gerador_de_codigo

    def adicionar(self, produto):
        produto.codigo = self.gerador_de_codigo.gerar()
        self.produtos.append(produto)

class GeradorDeCodigo:
    def __init__(self):
        self.codigo = 0

    def gerar(self):
        self.codigo += 1
        return self.codigo

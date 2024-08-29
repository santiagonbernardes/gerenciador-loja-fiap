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

    def obtenha(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def listar(self):
        return self.produtos


class GeradorDeCodigo:
    def __init__(self):
        self.codigo = 0

    def gerar(self):
        self.codigo += 1
        return self.codigo


class Estoque:
    def __init__(self):
        self.produtos_estocados = {}

    def adicionar(self, produto, quantidade):
        # TODO: Adicionar validacão para quantidade negativa.
        codigo_produto = produto.codigo
        if codigo_produto in self.produtos_estocados:
            self.produtos_estocados[codigo_produto] += quantidade
        else:
            self.produtos_estocados[codigo_produto] = quantidade

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

    def quantidade_estocada(self, produto):
        return self.produtos_estocados.get(produto.codigo, 0)

    def remover(self, produto, quantidade):
        codigo_produto = produto.codigo
        if codigo_produto in self.produtos_estocados:
            # TODO: lancar excecao caso a quantidade a ser removida seja maior que a quantidade em estoque ou negativo
            self.produtos_estocados[codigo_produto] -= quantidade
        else:
            # TODO: deve lancar excecao
            print(f'Produto#{produto.codigo} não está no estoque.')

    def atualizar(self, produto, nova_quantidade):
        codigo_produto = produto.codigo
        if codigo_produto in self.produtos_estocados:
            # TODO: lancar excecao se quantidade for negativa
            self.produtos_estocados[codigo_produto] = nova_quantidade
        else:
            # TODO: deve lancar excecao
            print(f'Produto#{produto.codigo} não está no estoque.')

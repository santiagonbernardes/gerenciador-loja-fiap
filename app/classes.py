from app.excecoes import NaoHaProdutosException


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
    def __init__(self, limite_estoque_baixo=3):
        self.produtos_estocados = {}
        self.limite_estoque_baixo = limite_estoque_baixo

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
            if self.produtos_estocados[codigo_produto] < self.limite_estoque_baixo:
                print(f'Atenção: o produto#{codigo_produto} está com estoque baixo.')
        else:
            # TODO: deve lancar excecao
            print(f'Produto#{produto.codigo} não está no estoque.')

    def atualizar(self, produto, nova_quantidade):
        codigo_produto = produto.codigo
        if codigo_produto in self.produtos_estocados:
            # TODO: lancar excecao se quantidade for negativa
            self.produtos_estocados[codigo_produto] = nova_quantidade

            if self.produtos_estocados[codigo_produto] < self.limite_estoque_baixo:
                print(f'Atenção: o produto#{codigo_produto} está com estoque menor que {self.limite_estoque_baixo}.')
        else:
            # TODO: deve lancar excecao
            print(f'Produto#{produto.codigo} não está no estoque.')


class ConversorDeInput:
    def __init__(self, texto_ao_usuario):
        self.texto_ao_usuario = texto_ao_usuario

    def converta(self):
        while True:
            try:
                entrada_do_usuario = input(self.texto_ao_usuario)
                return self.converta_para_o_tipo(entrada_do_usuario)
            except NotImplementedError as erro:
                raise erro
            except Exception:
                print('O dado que você digitou não é válido.')

    def converta_para_o_tipo(self, entrada_do_usuario):
        raise NotImplementedError('Você está chamando a classe errada, corrija seu código')


class ConversorDeInputFloat(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario):
        return float(entrada_do_usuario)


class ConversorDeInputInt(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario):
        return int(entrada_do_usuario)


class ConversorDeInputIntPositivo(ConversorDeInputInt):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario):
        valor_convertido = int(entrada_do_usuario)
        if valor_convertido < 1:
            raise Exception('Valor não é positivo')

        return valor_convertido


class ConversorDeInputFloatPositivo(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario):
        valor_convertido = float(entrada_do_usuario)
        if valor_convertido < 1:
            raise Exception('Valor não é positivo')

        return valor_convertido


class ConversorDeInputStringObrigatoria(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario):
        if entrada_do_usuario is None or entrada_do_usuario.strip() == '':
            raise Exception('String é obrigatória')

        return str(entrada_do_usuario)


class ExibidorDeProdutos:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def exiba_todos(self):
        produtos = self.repositorio.listar()

        if len(produtos) == 0:
            raise NaoHaProdutosException()

        for produto in produtos:
            print(f'{produto.codigo} - {produto.nome}')


conversores = {
    'int': ConversorDeInputInt,
    'float': ConversorDeInputFloat,
    'int_pos': ConversorDeInputIntPositivo,
    'float_pos': ConversorDeInputFloatPositivo,
    'str_obg': ConversorDeInputStringObrigatoria
}

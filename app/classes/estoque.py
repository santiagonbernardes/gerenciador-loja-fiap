from typing import Callable, Any

from app.classes.produto import Produto
from app.classes.rastreador import Rastreador
from app.excecoes import ProdutoSemEstoqueException, RemocaoMaiorQueEstoqueException, ProdutoNaoEstocadoException


class Estoque:

    def __init__(self, rastreador: Rastreador, limite_estoque_baixo: int = 3) -> None:
        self.produtos_estocados: dict[int, int] = {}
        self.limite_estoque_baixo: int = limite_estoque_baixo
        self.rastreador: Rastreador = rastreador

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        self.execute_com_logica_adicional(self.execute_adicionar, produto, quantidade, 'adicionar')

    def remover(self, produto: Produto, quantidade_remover: int) -> None:
        self.execute_com_logica_adicional(self.execute_remover, produto, quantidade_remover, 'remover')

    def atualizar(self, produto: Produto, nova_quantidade: int) -> None:
        self.execute_com_logica_adicional(self.execute_atualizar, produto, nova_quantidade, 'atualizar')

    def obtenha_quantidade_estocada(self, produto: Produto) -> int:
        codigo_produto: int = produto.codigo
        if codigo_produto not in self.produtos_estocados:
            raise ProdutoNaoEstocadoException()
        return self.produtos_estocados[codigo_produto]

    def atualize_limite_estoque_baixo(self, novo_limite: int) -> None:
        self.limite_estoque_baixo = novo_limite
        for codigo_produto, quantidade in self.produtos_estocados.items():
            if quantidade < novo_limite:
                self.mostre_mensagem_estoque_baixo(codigo_produto)

    # Daqui pra baixo, tudo deveria ser privado

    def execute_com_logica_adicional(self, funcao: Callable, *args: Any) -> None:
        # Esta funcão executará a função passada como parâmetro e verificará se o estoque está baixo para notificar
        # o usuário. O único requisito é que o primeiro parâmetro da função a ser executada seja o produto.
        produto: Produto = args[0]  # Produto tem que ser o primeiro parâmetro
        quantidade_entrada: int = args[1]  # Quantidade tem que ser o segundo parâmetro
        evento: str = args[-1]  # Evento tem que ser o último
        quantidade_original: int = 0

        try:
            quantidade_original = self.obtenha_quantidade_estocada(produto)
        except ProdutoNaoEstocadoException:
            pass

        funcao(*args)

        codigo_produto: int = produto.codigo
        if self.produtos_estocados[codigo_produto] < self.limite_estoque_baixo:
            self.mostre_mensagem_estoque_baixo(codigo_produto)

        self.rastreador.rastreie(self, produto, evento, quantidade_entrada, quantidade_original)

    def execute_adicionar(self, produto: Produto, quantidade: int, nome_evento: str) -> None:
        codigo_produto: int = produto.codigo
        if codigo_produto in self.produtos_estocados:
            self.produtos_estocados[codigo_produto] += quantidade
        else:
            self.execute_atualizar(produto, quantidade, nome_evento)

    def execute_remover(self, produto: Produto, quantidade_remover: int, nome_evento: str) -> None:
        codigo_produto: int = produto.codigo

        if codigo_produto not in self.produtos_estocados:
            raise ProdutoSemEstoqueException()

        if quantidade_remover > self.produtos_estocados[codigo_produto]:
            raise RemocaoMaiorQueEstoqueException()

        self.produtos_estocados[codigo_produto] -= quantidade_remover

    def execute_atualizar(self, produto: Produto, nova_quantidade: int, nome_evento: str) -> None:
        codigo_produto: int = produto.codigo
        self.produtos_estocados[codigo_produto] = nova_quantidade

    def mostre_mensagem_estoque_baixo(self, codigo_produto: int) -> None:
        estoque_atual: int = self.produtos_estocados[codigo_produto]
        print(f'Atenção: o produto#{codigo_produto} está com estoque baixo. Estoque atual é: {estoque_atual}.')

    def avise_de_evento(self, event: str):
        print(f'Evento: {event}')
        return None

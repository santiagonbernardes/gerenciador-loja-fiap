from app.classes.conversor_de_input import conversores
from app.classes.estoque import Estoque
from app.classes.exibidor_de_produtos import ExibidorDeProdutos
from app.classes.gerador_de_codigo import GeradorDeCodigo
from app.classes.produto import Produto
from app.classes.repositorio import Repositorio, RepositorioEmMemoria
from app.excecoes import ProdutoSemEstoqueException

repositorio_produtos: Repositorio = RepositorioEmMemoria[Produto](GeradorDeCodigo())
estoque: Estoque = Estoque()
exibidor: ExibidorDeProdutos = ExibidorDeProdutos(repositorio_produtos, estoque)


def obtenha_opcao_do_menu() -> int:
    print()
    print('O que você deseja fazer?\n')
    print('1 - Criar um produto')
    print('2 - Aumentar a quantidade de um produto no estoque')
    print('3 - Remover uma quantidade de um produto do estoque')
    print('4 - Ajustar manualmente a quantidade de um produto no estoque')
    print(f'5 - Alterar alerta de estoque baixo (valor atual: {estoque.limite_estoque_baixo})')
    print('0 - Sair')
    return conversores['int']('Escolha uma opção: ').converta()


def obtenha_produto(repositorio: Repositorio,
                    estoque: Estoque,
                    exibidor: ExibidorDeProdutos,
                    erro_estoque_vazio: bool = False) -> Produto:
    produto_encontrado: Produto | None = None

    while not produto_encontrado:
        exibidor.exiba_todos()

        codigo_produto: int = conversores['int']('\nInforme o código do produto: ').converta()
        produto_encontrado: Produto = repositorio.obtenha(codigo_produto)

        if not produto_encontrado:
            print(f'\nProduto#{codigo_produto} não encontrado. Informe um código de produto existente')

    quantidade_estocada: int = estoque.obtenha_quantidade_estocada(produto_encontrado)

    if erro_estoque_vazio and quantidade_estocada == 0:
        raise ProdutoSemEstoqueException()

    print(f'O produto {produto_encontrado.nome} possui {quantidade_estocada} unidades em estoque.')

    return produto_encontrado


def crie_produto() -> None:
    nome: str = conversores['str_obg']('Informe o nome do produto: ').converta()
    categoria: str = conversores['str_obg']('Informe a categoria do produto: ').converta()
    preco: float = conversores['float_pos']('Informe o preço do produto: ').converta()
    descricao: str = conversores['str_obg']('Informe a descrição do produto: ').converta()
    fornecedor: str = conversores['str_obg']('Informe o fornecedor do produto: ').converta()

    produto: Produto = Produto(nome, categoria, preco, descricao, fornecedor)
    repositorio_produtos.adicionar(produto)
    estoque.adicionar(produto, 0)

    print(f'\nProduto#{produto.codigo} criado com sucesso!')


def adicione_ao_estoque() -> None:
    produto: Produto = obtenha_produto(repositorio_produtos, estoque, exibidor)
    quantidade: int = conversores['int_pos']('Informe a quantidade a ser adicionada ao estoque: ').converta()
    estoque.adicionar(produto, quantidade)
    print(f'\nQuantidade de {quantidade} adicionada ao estoque do produto#{produto.codigo}.')


def remova_do_estoque() -> None:
    produto: Produto = obtenha_produto(repositorio_produtos, estoque, exibidor, erro_estoque_vazio=True)
    quantidade_remover: int = conversores['int_pos'](
        'Informe a quantidade a ser removida do estoque: ').converta()
    estoque.remover(produto, quantidade_remover)
    print(f'\nQuantidade de {quantidade_remover} removida do estoque do produto#{produto.codigo}.')


def ajuste_estoque_manualmente() -> None:
    produto: Produto = obtenha_produto(repositorio_produtos, estoque, exibidor)
    nova_quantidade: int = conversores['int_pos']('Informe a nova quantidade do produto no estoque: ').converta()
    estoque.atualizar(produto, nova_quantidade)
    print(f'\nQuantidade do produto#{produto.codigo} atualizada para {nova_quantidade}.')


def altere_alerta_estoque() -> None:
    alerta_original: int = estoque.limite_estoque_baixo
    print(f'O valor atual do alerta de estoque baixo é {alerta_original}.')
    novo_alerta: int = conversores['int_pos']('Informe o novo valor do alerta de estoque baixo: ').converta()
    estoque.atualize_limite_estoque_baixo(novo_alerta)
    print(f'Alerta de estoque baixo alterado de {alerta_original} para {novo_alerta}.')

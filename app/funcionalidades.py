from tabulate import tabulate

from app.classes.conversor_de_input import conversores
from app.classes.cupom import Cupom
from app.classes.estoque import Estoque
from app.classes.exibidor_de_cupons import ExibidorDeCupons
from app.classes.exibidor_de_produtos import ExibidorDeProdutos
from app.classes.exibidor_de_venda import ExibidorDeVenda
from app.classes.gerador_de_codigo import GeradorDeCodigo
from app.classes.produto import Produto
from app.classes.rastreador import Evento, Rastreador
from app.classes.repositorio import Repositorio, RepositorioEmMemoria
from app.classes.venda import Venda
from app.excecoes import ProdutoSemEstoqueException

gerador: GeradorDeCodigo = GeradorDeCodigo()
repositorio_produtos: Repositorio = RepositorioEmMemoria[Produto](gerador)
repositorio_vendas: Repositorio = RepositorioEmMemoria[Venda](gerador)
repositorio_cupons: Repositorio = RepositorioEmMemoria[Cupom](gerador)
repositorio_eventos: Repositorio = RepositorioEmMemoria[Evento](gerador)
rastrador: Rastreador = Rastreador(repositorio_eventos)
estoque: Estoque = Estoque(rastrador)
exibidor_de_produtos: ExibidorDeProdutos = ExibidorDeProdutos(repositorio_produtos, estoque)
exibidor_de_cupons: ExibidorDeCupons = ExibidorDeCupons(repositorio_cupons)


def obtenha_opcao_do_menu() -> int:
    print()
    print('O que você deseja fazer?\n')
    print('1 - Criar um produto')
    print('2 - Aumentar a quantidade de um produto no estoque')
    print('3 - Remover uma quantidade de um produto do estoque')
    print('4 - Ajustar manualmente a quantidade de um produto no estoque')
    print(f'5 - Alterar alerta de estoque baixo (valor atual: {estoque.limite_estoque_baixo})')
    print('6 - Fazer uma venda')
    print('7 - Listar cupons')
    print('8 - Criar um cupom')
    print('9 - Emitir relatório de vendas')
    print('10 - Emitir relatório do estoque')
    print('11 - Exibe relatório de movimentacão do estoque')
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

    produto = crie_produto_com_estoque(categoria, descricao, fornecedor, nome, preco)

    print(f'\nProduto#{produto.codigo} criado com sucesso!')


def crie_produto_com_estoque(categoria: str, descricao: str, fornecedor: str, nome: str, preco: float,
                             quantidade: int = 0):
    produto: Produto = Produto(nome, categoria, preco, descricao, fornecedor)
    repositorio_produtos.adicionar(produto)
    estoque.adicionar(produto, quantidade)
    return produto


def adicione_ao_estoque() -> None:
    produto: Produto = obtenha_produto(repositorio_produtos, estoque, exibidor_de_produtos)
    quantidade: int = conversores['int_pos']('Informe a quantidade a ser adicionada ao estoque: ').converta()
    estoque.adicionar(produto, quantidade)
    print(f'\nQuantidade de {quantidade} adicionada ao estoque do produto#{produto.codigo}.')


def remova_do_estoque() -> None:
    produto: Produto = obtenha_produto(repositorio_produtos, estoque, exibidor_de_produtos, erro_estoque_vazio=True)
    quantidade_remover: int = conversores['int_pos'](
        'Informe a quantidade a ser removida do estoque: ').converta()
    estoque.remover(produto, quantidade_remover)
    print(f'\nQuantidade de {quantidade_remover} removida do estoque do produto#{produto.codigo}.')


def ajuste_estoque_manualmente() -> None:
    produto: Produto = obtenha_produto(repositorio_produtos, estoque, exibidor_de_produtos)
    nova_quantidade: int = conversores['int_pos']('Informe a nova quantidade do produto no estoque: ').converta()
    estoque.atualizar(produto, nova_quantidade)
    print(f'\nQuantidade do produto#{produto.codigo} atualizada para {nova_quantidade}.')


def altere_alerta_estoque() -> None:
    alerta_original: int = estoque.limite_estoque_baixo
    print(f'O valor atual do alerta de estoque baixo é {alerta_original}.')
    novo_alerta: int = conversores['int_pos']('Informe o novo valor do alerta de estoque baixo: ').converta()
    estoque.atualize_limite_estoque_baixo(novo_alerta)
    print(f'Alerta de estoque baixo alterado de {alerta_original} para {novo_alerta}.')


def obtenha_opcao_venda() -> int:
    print()
    print('Selecione 0 para finalizar a venda ou qualquer outro número positivo para continuar adicionando produtos.')
    return conversores['int']('Escolha uma opção: ').converta()


def faca_venda():
    opcao: int = -1
    venda: Venda = Venda()
    while opcao != 0:
        try:
            produto: Produto = obtenha_produto(repositorio_produtos, estoque, exibidor_de_produtos,
                                               erro_estoque_vazio=True)
        except ProdutoSemEstoqueException:
            print('Produto sem unidades em estoque.')
            opcao = obtenha_opcao_venda()
            continue

        quantidade_venda: int = conversores['int_pos']('Informe a quantidade a ser vendida: ').converta()
        if quantidade_venda > estoque.obtenha_quantidade_estocada(produto):
            print('O produto não possui esta quantidade em estoque.')
            opcao = obtenha_opcao_venda()
            continue

        estoque.remover(produto, quantidade_venda)
        venda.adicione_item(produto, quantidade_venda)

        opcao = obtenha_opcao_venda()

    if len(venda.itens) == 0:
        print('Venda cancelada, nenhum item foi adicionado.')
    else:
        opcao_aplicar_cupom: str = conversores['str_s_n']('Deseja aplicar um cupom (s/n)? ').converta()
        if opcao_aplicar_cupom == 's':
            opcao_cupom: str = ""
            while opcao_cupom.lower() != "sair":
                opcao_cupom = conversores['str_obg']('Informe o nome do cupom ou "SAIR" para finalizar: ').converta()
                if opcao_cupom.lower() == "sair":
                    print(f'Saindo da aplicação de cupons.')
                else:
                    cupom: Cupom | None = None
                    for cupom_armazenado in repositorio_cupons.listar():
                        if cupom_armazenado.eh_valido(opcao_cupom):
                            cupom = cupom_armazenado

                    if cupom:
                        venda.cupom = cupom
                        print(f'Cupom {cupom.nome} aplicado com sucesso!')
                        break
                    else:
                        print(f'Cupom {opcao_cupom} não encontrado. Tente novamente')

        repositorio_vendas.adicionar(venda)
        print(f'\nVenda#{venda.codigo} realizada com sucesso!')

    print('\nEmitindo recibo da venda:\n')
    print(ExibidorDeVenda(venda, repositorio_produtos).exiba_todos())


def liste_cupons() -> None:
    exibidor_de_cupons.exiba_todos()


def crie_cupom() -> None:
    nome: str = conversores['str_obg']('Informe o nome: ').converta()
    descricao: str = conversores['str_obg']('Informe a descrição: ').converta()
    porcentagem_desconto: float = conversores['float_pos']('Informe a porcentagem de desconto do cupom: ').converta()

    for cupom_ja_criado in repositorio_cupons.listar():
        if cupom_ja_criado.eh_valido(nome):
            print(f'\nCupom com o identificador {nome} já existe.')
            return

    cupom: Cupom = Cupom(nome, descricao, porcentagem_desconto)
    repositorio_cupons.adicionar(cupom)
    print(f'\nCupom#{cupom.codigo} criado com sucesso!')


def emite_relatorio_vendas() -> None:
    vendas = repositorio_vendas.listar()
    if len(vendas) == 0:
        print('Não há vendas realizadas.')
        return

    print('\nRelatório de vendas:\n')
    for venda in vendas:
        print(ExibidorDeVenda(venda, repositorio_produtos).exiba_todos())


def emite_relatorio_estoque() -> None:
    print('\nRelatório de estoque:\n')
    print(exibidor_de_produtos.exiba_todos(mostra_produtos_disponiveis=False))


def emite_relatorio_movimentacao_estoque() -> None:
    dados = []
    for evento in repositorio_eventos.listar():
        dados.append([evento.data, evento.evento, evento.codigo_produto, evento.quantidade_original,
                      evento.quantidade_entrada, evento.quantidade_atualizada])
    headers = ['Data', 'Evento', 'Código Produto', 'Quantidade Original', 'Quantidade modificada',
               'Quantidade Atualizada']
    print('\nRelatório de movimentação de estoque:\n')
    print(tabulate(dados, headers=headers, tablefmt='pretty'))


def popule_banco() -> None:
    produtos = [
        ("Apple iPhone 13", "Eletrônicos", 799.0, "Smartphone Apple iPhone 13 com 128GB", "Apple", 50),
        ("Samsung Galaxy S21", "Eletrônicos", 699.0, "Smartphone Samsung Galaxy S21 com 128GB", "Samsung", 30),
        ("Sony WH-1000XM4", "Acessórios", 349.0, "Fone de Ouvido Sony WH-1000XM4 c/ Cancelamento de Ruído", "Sony", 20),
        ("Dell XPS 13", "Computadores", 999.0, "Notebook Dell XPS 13 com Intel i7 e 16GB RAM", "Dell", 10),
        ("Apple MacBook Pro", "Computadores", 1299.0, "Notebook Apple MacBook Pro com M1 Chip", "Apple", 5),
        ("Logitech MX Master 3", "Acessórios", 99.0, "Mouse Logitech MX Master 3", "Logitech", 8),
        ("Amazon Echo Dot", "Casa Inteligente", 49.0, "Assistente Virtual Amazon Echo Dot 4ª Geração", "Amazon", 12),
        ("Google Nest Hub", "Casa Inteligente", 89.0, "Assistente Virtual Google Nest Hub", "Google", 7),
        ("Sony PlayStation 5", "Games", 499.0, "Console Sony PlayStation 5", "Sony", 3),
        ("Microsoft Xbox Series X", "Games", 499.0, "Console Microsoft Xbox Series X", "Microsoft", 1),
    ]

    for nome, categoria, preco, descricao, fornecedor, quantidade in produtos:
        crie_produto_com_estoque(categoria, descricao, fornecedor, nome, preco, quantidade)

    cupons = [
        ("ESSEVALE10", "Desconto de 10%", 10.0),
        ("PYTHON", "Desconto de 20%", 20.0),
        ("FIAP", "Desconto de 30%", 30.0),
        ("DESC40", "Desconto de 40%", 40.0),
        ("FICOUDOIDO", "Desconto de 50%", 50.0),
    ]

    for descricao, identificador, porcentagem_desconto in cupons:
        repositorio_cupons.adicionar(Cupom(descricao, identificador, porcentagem_desconto))

    print("Banco de dados populado com 10 produtos e 5 cupons.")

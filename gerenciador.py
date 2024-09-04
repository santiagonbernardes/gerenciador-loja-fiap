from app.classes import Produto, Repositorio, GeradorDeCodigo, Estoque, conversores, ExibidorDeProdutos
from app.excecoes import NaoHaProdutosException, ProdutoSemEstoqueException, RemocaoMaiorQueEstoqueException

repositorio = Repositorio(GeradorDeCodigo())
estoque = Estoque()
exibidor = ExibidorDeProdutos(repositorio)


def obtenha_produto(repositorio, estoque, exibidor, erro_estoque_vazio=False):
    produto_encontrado = None

    while not produto_encontrado:
        exibidor.exiba_todos()

        codigo_produto = conversores['int']('\nInforme o código do produto: ').converta()
        produto_encontrado = repositorio.obtenha(codigo_produto)

        if not produto_encontrado:
            print(f'\nProduto#{codigo_produto} não encontrado. Informe um código de produto existente')

    quantidade_estocada = estoque.quantidade_estocada(produto_encontrado)

    if erro_estoque_vazio and quantidade_estocada == 0:
        raise ProdutoSemEstoqueException()

    print(f'O produto {produto_encontrado.nome} possui {quantidade_estocada} unidades em estoque.')

    return produto_encontrado


if __name__ == '__main__':
    opcao = -1
    print('Bem vindo ao gerenciador de loja de varejo da FIAP.\n')
    while opcao != 0:
        try:
            print()
            print('O que você deseja fazer?\n')
            print('1 - Criar um produto')
            print('2 - Aumentar a quantidade de um produto no estoque')
            print('3 - Remover uma quantidade de um produto do estoque')
            print('4 - Ajustar manualmente a quantidade de um produto no estoque')
            print(f'5 - Alterar alerta de estoque baixo (valor atual: {estoque.limite_estoque_baixo})')
            print('0 - Sair')
            opcao = conversores['int']('Escolha uma opção: ').converta()
            print()
            if opcao == 0:
                # Sair
                print('Obrigado por usar o gerenciador de loja de varejo da FIAP.')
            elif opcao == 1:
                # Criar produto
                nome = conversores['str_obg']('Informe o nome do produto: ').converta()
                categoria = conversores['str_obg']('Informe a categoria do produto: ').converta()
                preco = conversores['float_pos']('Informe o preço do produto: ').converta()
                descricao = conversores['str_obg']('Informe a descrição do produto: ').converta()
                fornecedor = conversores['str_obg']('Informe o fornecedor do produto: ').converta()

                produto = Produto(nome, categoria, preco, descricao, fornecedor)
                repositorio.adicionar(produto)

                print(f'\nProduto#{produto.codigo} criado com sucesso!')
            elif opcao == 2:
                # Adicionar produtos ao estoque
                produto = obtenha_produto(repositorio, estoque, exibidor)
                quantidade = conversores['int_pos']('Informe a quantidade a ser adicionada ao estoque: ').converta()
                estoque.adicionar(produto, quantidade)
                print(f'\nQuantidade de {quantidade} adicionada ao estoque do produto#{produto.codigo}.')
            elif opcao == 3:
                # Remover itens do estoque
                produto = obtenha_produto(repositorio, estoque, exibidor, erro_estoque_vazio=True)
                quantidade_remover = conversores['int_pos'](
                    'Informe a quantidade a ser removida do estoque: ').converta()
                estoque.remover(produto, quantidade_remover)
                print(f'\nQuantidade de {quantidade_remover} removida do estoque do produto#{produto.codigo}.')
            elif opcao == 4:
                # Ajustar manualmente a quantidade de um produto no estoque
                produto = obtenha_produto(repositorio, estoque, exibidor)
                nova_quantidade = conversores['int_pos']('Informe a nova quantidade do produto no estoque: ').converta()
                estoque.atualizar(produto, nova_quantidade)
                print(f'\nQuantidade do produto#{produto.codigo} atualizada para {nova_quantidade}.')
            elif opcao == 5:
                # Alterar alerta de estoque baixo
                alerta_original = estoque.limite_estoque_baixo
                print(f'O valor atual do alerta de estoque baixo é {alerta_original}.')
                novo_alerta = conversores['int_pos']('Informe o novo valor do alerta de estoque baixo: ').converta()
                estoque.limite_estoque_baixo = novo_alerta
                print(f'Alerta de estoque baixo alterado de {alerta_original} para {novo_alerta}.')
            else:
                print(f'Opção {opcao} inválida.')
        except NaoHaProdutosException:
            print('Não há produtos criados.')
        except ProdutoSemEstoqueException:
            print('Produto sem unidades em estoque.')
        except RemocaoMaiorQueEstoqueException:
            print('Quantidade a remover maior que a quantidade em estoque.')

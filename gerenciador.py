from app.classes import Produto, Repositorio, GeradorDeCodigo, Estoque, conversores

repositorio = Repositorio(GeradorDeCodigo())
estoque = Estoque()

if __name__ == '__main__':
    opcao = -1
    print('Bem vindo ao gerenciador de loja de varejo da FIAP.\n')
    while opcao != 0:
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
            nome = input('Informe o nome do produto: ')
            categoria = input('Informe a categoria do produto: ')
            preco = conversores['float_pos']('Informe o preço do produto: ').converta()
            descricao = input('Informe a descrição do produto: ')
            fornecedor = input('Informe o fornecedor do produto: ')

            produto = Produto(nome, categoria, preco, descricao, fornecedor)
            repositorio.adicionar(produto)

            print(f'\nProduto#{produto.codigo} criado com sucesso!')
        elif opcao == 2:
            # Adicionar produtos ao estoque
            produtos_criados = repositorio.listar()

            if len(produtos_criados) == 0:
                print('Não há produtos criados.')
                continue

            print('Produtos existentes:\n')
            for produto in produtos_criados:
                print(f'{produto.codigo} - {produto.nome}')

            codigo_produto = conversores['int']('\nInforme o código do produto: ').converta()
            produto = repositorio.obtenha(codigo_produto)

            if not produto:
                print(f'\nProduto#{codigo_produto} não encontrado. Informe um código de produto existente')
                continue

            quantidade_estocada = estoque.quantidade_estocada(produto)

            print(f'O produto {produto.nome} possui {quantidade_estocada} unidades em estoque.')

            quantidade = conversores['int_pos']('Informe a quantidade a ser adicionada ao estoque: ').converta()

            estoque.adicionar(produto, quantidade)

            print(f'\nQuantidade de {quantidade} adicionada ao estoque do produto#{codigo_produto}.')
        elif opcao == 3:
            # Remover itens do estoque
            produtos_criados = repositorio.listar()

            if len(produtos_criados) == 0:
                print('Não há produtos criados.')
                continue

            print('Produtos existentes:\n')
            for produto in produtos_criados:
                print(f'{produto.codigo} - {produto.nome}')

            codigo_produto = conversores['int']('\nInforme o código do produto: ').converta()
            produto = repositorio.obtenha(codigo_produto)

            if not produto:
                print(f'\nProduto#{codigo_produto} não encontrado. Informe um código de produto existente')
                continue

            quantidade_estocada = estoque.quantidade_estocada(produto)

            if quantidade_estocada == 0:
                print(f'O produto#{produto.codigo} não possui unidades em estoque.')
                continue

            print(f'O produto {produto.nome} possui {quantidade_estocada} unidades em estoque.')

            quantidade_remover = conversores['int_pos']('Informe a quantidade a ser removida do estoque: ').converta()

            estoque.remover(produto, quantidade_remover)

            # TODO: tratar excecao de remoćão aqui
            print(f'\nQuantidade de {quantidade_remover} removida do estoque do produto#{codigo_produto}.')
        elif opcao == 4:
            # Ajustar manualmente a quantidade de um produto no estoque
            produtos_criados = repositorio.listar()

            if len(produtos_criados) == 0:
                print('Não há produtos criados.')
                continue

            print('Produtos existentes:\n')
            for produto in produtos_criados:
                print(f'{produto.codigo} - {produto.nome}')

            codigo_produto = conversores['int']('\nInforme o código do produto: ').converta()
            produto = repositorio.obtenha(codigo_produto)

            if not produto:
                print(f'\nProduto#{codigo_produto} não encontrado. Informe um código de produto existente')
                continue

            quantidade_estocada = estoque.quantidade_estocada(produto)

            print(f'O produto {produto.nome} possui {quantidade_estocada} unidades em estoque.')

            nova_quantidade = conversores['int_pos']('Informe a nova quantidade do produto no estoque: ').converta()

            estoque.atualizar(produto, nova_quantidade)

            print(
                f'\nQuantidade do produto#{produto.codigo} atualizada de {quantidade_estocada} para {nova_quantidade}.'
            )
        elif opcao == 5:
            # Alterar alerta de estoque baixo
            alerta_original = estoque.limite_estoque_baixo
            print(f'O valor atual do alerta de estoque baixo é {alerta_original}.')
            novo_alerta = conversores['int_pos']('Informe o novo valor do alerta de estoque baixo: ').converta()
            estoque.limite_estoque_baixo = novo_alerta
            print(f'Alerta de estoque baixo alterado de {alerta_original} para {novo_alerta}.')
        else:
            print(f'Opção {opcao} inválida.')

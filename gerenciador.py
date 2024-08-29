from app.classes import Produto, Repositorio, GeradorDeCodigo, Estoque

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
        print('0 - Sair')
        # TODO: adicionar exceção para caso o usuário digite um valor que não seja um número
        opcao = int(input('Escolha uma opção: '))
        print()
        if opcao == 0:
            print('Obrigado por usar o gerenciador de loja de varejo da FIAP.')
        elif opcao == 1:
            nome = input('Informe o nome do produto: ')
            categoria = input('Informe a categoria do produto: ')
            # TODO: adicionar tratamento de excecão para o preco
            preco = float(input('Informe o preço do produto: '))
            descricao = input('Informe a descrição do produto: ')
            fornecedor = input('Informe o fornecedor do produto: ')

            produto = Produto(nome, categoria, preco, descricao, fornecedor)
            repositorio.adicionar(produto)

            print(f'\nProduto#{produto.codigo} criado com sucesso!')
        elif opcao == 2:
            produtos_criados = repositorio.listar()

            if len(produtos_criados) == 0:
                print('Não há produtos criados.')
                continue

            print('Produtos existentes:\n')
            for produto in produtos_criados:
                print(f'{produto.codigo} - {produto.nome}')

            codigo_produto = int(input('\nInforme o código do produto: '))
            produto = repositorio.obtenha(codigo_produto)

            if not produto:
                print(f'\nProduto#{codigo_produto} não encontrado. Informe um código de produto existente')
                continue

            # TODO: adicionar validacão de input inválido
            quantidade = int(input('Informe a quantidade a ser adicionada ao estoque: '))

            estoque.adicionar(produto, quantidade)

            print(f'\nQuantidade de {quantidade} adicionada ao estoque do produto#{codigo_produto}.')

from app.classes import Produto

if __name__ == '__main__':
    opcao = -1
    print('Bem vindo ao gerenciador de loja de varejo da FIAP.\n')
    while opcao != 0:
        print()
        print('O que você deseja fazer?\n')
        print('1 - Criar um produto')
        print('0 - Sair')
        # TODO: adicionar exceção para caso o usuário digite um valor que não seja um número
        opcao = int(input('Escolha uma opção: '))
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

            print('\nProduto criado com sucesso!')

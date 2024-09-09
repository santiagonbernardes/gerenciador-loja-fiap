from app.excecoes import NaoHaProdutosException, ProdutoSemEstoqueException, RemocaoMaiorQueEstoqueException, \
    ProdutoNaoEstocadoException
from app.funcionalidades import crie_produto, adicione_ao_estoque, remova_do_estoque, ajuste_estoque_manualmente, \
    altere_alerta_estoque, obtenha_opcao_do_menu

if __name__ == '__main__':
    opcao: int = -1
    print('Bem vindo ao gerenciador de loja de varejo da FIAP.\n')
    while opcao != 0:
        try:
            opcao = obtenha_opcao_do_menu()
            print()
            if opcao == 0:
                # Sair
                print('Obrigado por usar o gerenciador de loja de varejo da FIAP.')
            elif opcao == 1:
                # Criar produto
                crie_produto()
            elif opcao == 2:
                # Adicionar produtos ao estoque
                adicione_ao_estoque()
            elif opcao == 3:
                # Remover itens do estoque
                remova_do_estoque()
            elif opcao == 4:
                # Ajustar manualmente a quantidade de um produto no estoque
                ajuste_estoque_manualmente()
            elif opcao == 5:
                # Alterar alerta de estoque baixo
                altere_alerta_estoque()
            else:
                print(f'Opção {opcao} inválida.')
        except NaoHaProdutosException:
            print('Não há produtos criados.')
        except ProdutoSemEstoqueException:
            print('Produto sem unidades em estoque.')
        except RemocaoMaiorQueEstoqueException:
            print('Quantidade a remover maior que a quantidade em estoque.')
        except ProdutoNaoEstocadoException:
            print('Você tentou acessar o estoque de um produto que não está estocado. Adicione o produto ao estoque.')

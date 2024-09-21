# Gerenciador de Lojas da FIAP

## Grupo

- [José Enrico dos Santos Tavares](https://github.com/joseenricotavares) - RM554471
- [Lucas Hidetoshi Ichiama](https://github.com/ichiamalucas) - RM555077
- [Mizael Vieira Bezerra](https://github.com/mizaelvieira1) - RM555796
- [Santiago Nascimento Bernardes](https://github.com/santiagonbernardes) - RM557447
- [Thiago Almança Da Silva](https://github.com/ThiagoSilva15) - RM558108

## Descrição

Este repositório mantém o código fonte do projeto de Gerenciador de Lojas da FIAP, desenvolvido para a disciplina de
Computational Thinking Using Python. O objetivo do projeto é criar um sistema gerenciador de loja de varejo com gestão
de estoque de produtos.

## Requisitos

1. Cadastro de Produtos
    - Nome do Produto: Campo para armazenar o nome do produto.
    - Código do Produto: Um código único para identificar o produto.
    - Categoria: Categorias como "eletrônicos", "vestuário", etc.
    - Quantidade em Estoque: Campo para armazenar a quantidade disponível no estoque.
    - Preço: Preço de venda do produto.
    - Descrição: Detalhes adicionais sobre o produto.
    - Fornecedor: Informações sobre o fornecedor do produto.
2. Gestão de Estoque
    - Adicionar ao Estoque: Funcionalidade para aumentar a quantidade de um produto no estoque.
    - Remover do Estoque: Funcionalidade para reduzir a quantidade de um produto no estoque.
    - Atualização de Estoque: Possibilidade de ajustar manualmente a quantidade de produtos.
    - Alerta de Estoque Baixo: Sistema de notificação quando a quantidade de um produto atinge um nível mínimo
      predefinido.
3. Vendas
    - Registro de Vendas: Função para registrar a venda de produtos.
    - Atualização Automática do Estoque: Ao registrar uma venda, a quantidade em estoque deve ser automaticamente reduzida.
    - Emissão de Recibo: Geração de um recibo ou nota fiscal após a venda.
    - Descontos e Promoções: Função para aplicar descontos específicos ou promoções a produtos.

4. Relatórios
    - Relatório de Vendas: Relatório detalhado das vendas realizadas, incluindo data, produtos vendidos, quantidade e valor total.
    - Relatório de Estoque: Visualização da quantidade atual de todos os produtos no estoque.
    - Histórico de Movimentações: Registro de todas as adições e remoções de estoque.


## Estrutura do Projeto

- app/
    - classes/
        - produto.py: classes referentes a produtos
        - estoque.py: classes referentes ao estoque
        - conversor_de_input.py: classes referentes a conversão de input, expondo um dicionário que age como "factory".
        - repositorio.py: define um repositório através de uma classe pai e implementa uma classe filha para salvar
          dados em memória
        - exibidor_de_produtos.py: classe que personaliza a exibição de produtos na linha de comando
        - gerador_de_codigo.py: classe que gera códigos únicos para itens salvos no repositório
        - cupom.py: classe que que modela um cupom
        - venda.py: classe que modela uma venda
        - exibidor_de_vendas.py: classe que personaliza a exibição de vendas na linha de comando
        - exibidor_de_cupons.py: classe que personaliza a exibição de cupons na linha de comando
        - persistente.py: define a superclasse de um objeto que pode ser persistido
        - rastreador.py: classe que rastreia a movimentação no estoque
    - excecoes.py: exceções personalizadas do sistema
    - funcionalidades.py: funções principais do sistema, baseadas nos requisitos. utilizado a partir do gerenciador.py
- Script principal que executa o gerenciador de loja, contendo o loop principal e a lógica de menu

## Requisitos para rodar o projeto

- Python 3.10 ou superior; ou
- Docker

## Rodando o projeto

Os passos a seguir são obrigatórios em qualquer uma das opcões:

1. Clone o repositório
2. Acesse a pasta do projeto usando o terminal

### Python

3. Execute o comando `python gerenciador.py`
4. Siga as instruções exibidas no terminal

### Docker

3. Execute o comando `docker run -it --rm -v $(pwd):/app -w /app python:3.10-slim sh -c "python gerenciador.py"`
4. Siga as instruções exibidas no terminal

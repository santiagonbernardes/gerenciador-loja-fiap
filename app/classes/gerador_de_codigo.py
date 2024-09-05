class GeradorDeCodigo:
    def __init__(self):
        self.codigo = 0

    def gerar(self):
        # Esta classe apenas incrementa o código, ou seja, caso um código seja gerado, ele não será mais reutilizado.
        self.codigo += 1
        return self.codigo

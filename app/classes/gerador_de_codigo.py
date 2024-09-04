class GeradorDeCodigo:
    def __init__(self):
        self.codigo = 0

    def gerar(self):
        self.codigo += 1
        return self.codigo

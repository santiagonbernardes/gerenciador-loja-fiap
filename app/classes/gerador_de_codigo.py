class GeradorDeCodigo:
    def __init__(self) -> None:
        self.codigo: int = 0

    def gerar(self) -> int:
        # Esta classe apenas incrementa o código, ou seja, caso um código seja gerado, ele não será mais reutilizado.
        self.codigo += 1
        return self.codigo

class Persistente:
    def __init__(self):
        self.codigo: int | None = None

    def set_codigo(self, codigo: int) -> None:
        self.codigo = codigo

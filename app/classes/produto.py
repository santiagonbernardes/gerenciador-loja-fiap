class Produto:

    def __init__(self, nome: str, categoria: str, preco: float, descricao: str, fornecedor: str) -> None:
        self.nome: str = nome
        self.categoria: str = categoria
        self.preco: float = preco
        self.descricao: str = descricao
        self.fornecedor: str = fornecedor
        self.codigo: int | None = None

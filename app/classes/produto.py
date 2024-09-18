from app.classes.persistente import Persistente

class Produto(Persistente):

    def __init__(self, nome: str, categoria: str, preco: float, descricao: str, fornecedor: str) -> None:
        super().__init__()
        self.nome: str = nome
        self.categoria: str = categoria
        self.preco: float = preco
        self.descricao: str = descricao
        self.fornecedor: str = fornecedor
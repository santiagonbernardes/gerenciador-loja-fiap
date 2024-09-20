from app.classes.persistente import Persistente


class Cupom(Persistente):
    def __init__(self, nome: str, descricao: str, porcentagem_desconto: float) -> None:
        super().__init__()
        self.nome: str = nome
        self.descricao: str = descricao
        self.porcentagem_desconto: float = porcentagem_desconto
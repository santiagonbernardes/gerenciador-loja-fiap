from typing import TypeVar, Generic

from app.classes.gerador_de_codigo import GeradorDeCodigo
from app.classes.persistente import Persistente

T = TypeVar('T', bound=Persistente)


class Repositorio(Generic[T]):
    def __init__(self, gerador_de_codigo: GeradorDeCodigo) -> None:
        self.gerador_de_codigo = gerador_de_codigo

    def adicionar(self, item: T) -> None:
        item.set_codigo(self.gerador_de_codigo.gerar())
        self.salve(item)

    def obtenha(self, codigo: int) -> T:
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')

    def listar(self) -> list[T]:
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')

    # Daqui pra baixo, tudo deveria ser privado ou protegido
    def salve(self, item: T) -> None:
        raise NotImplementedError('Você está chamando a super classe, corrija seu código')


class RepositorioEmMemoria(Repositorio[T]):
    def __init__(self, gerador_de_codigo: GeradorDeCodigo) -> None:
        super().__init__(gerador_de_codigo)
        self.itens: list[T] = []

    def obtenha(self, codigo: int) -> T | None:
        for item in self.itens:
            if item.codigo == codigo:
                return item
        return None

    def listar(self) -> list[T]:
        return self.itens

    def salve(self, item: T) -> None:
        self.itens.append(item)

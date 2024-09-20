from tabulate import tabulate

from app.classes.cupom import Cupom
from app.classes.repositorio import Repositorio
from app.excecoes import NaoHaCuponsException


class ExibidorDeCupons:
    def __init__(self, repositorio: Repositorio) -> None:
        self.repositorio: Repositorio = repositorio
        self.headers: list[str] = ['Código', 'Nome', 'Descricão', 'Preço']

    def exiba_todos(self) -> None:
        cupons: list[Cupom] = self.repositorio.listar()

        if len(cupons) == 0:
            raise NaoHaCuponsException()

        dados = []

        for cupom in cupons:
            dados.append([cupom.codigo, cupom.nome, cupom.descricao, f'{cupom.porcentagem_desconto}%'])

        print('Cupons disponíveis:\n')
        print(tabulate(dados, headers=self.headers, tablefmt='pretty'))

class ConversorDeInput:
    def __init__(self, texto_ao_usuario: str) -> None:
        self.texto_ao_usuario: str = texto_ao_usuario

    def converta(self) -> str | int | float:
        while True:
            try:
                entrada_do_usuario: str = input(self.texto_ao_usuario)
                return self.converta_para_o_tipo(entrada_do_usuario)
            except NotImplementedError as erro:
                raise erro
            except Exception:
                print('O dado que você digitou não é válido.')

    # Daqui pra baixo, tudo deveria ser privado ou protegido
    def converta_para_o_tipo(self, entrada_do_usuario: str) -> str | int | float:
        # Este método deve ser implementado pelas classes filhas para que o método converta funcione
        raise NotImplementedError('Você está chamando a classe errada, corrija seu código')


class ConversorDeInputFloat(ConversorDeInput):
    def __init__(self, texto_ao_usuario: str) -> None:
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario: str) -> float:
        return float(entrada_do_usuario)


class ConversorDeInputInt(ConversorDeInput):
    def __init__(self, texto_ao_usuario: str) -> None:
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario: str) -> int:
        return int(entrada_do_usuario)


class ConversorDeInputIntPositivo(ConversorDeInputInt):
    def __init__(self, texto_ao_usuario: str) -> None:
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario: str) -> int:
        valor_convertido = int(entrada_do_usuario)
        if valor_convertido < 1:
            raise Exception('Valor não é positivo')

        return valor_convertido


class ConversorDeInputFloatPositivo(ConversorDeInput):
    def __init__(self, texto_ao_usuario: str) -> None:
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario: str) -> float:
        valor_convertido = float(entrada_do_usuario)
        if valor_convertido < 1:
            raise Exception('Valor não é positivo')

        return valor_convertido


class ConversorDeInputStringObrigatoria(ConversorDeInput):
    def __init__(self, texto_ao_usuario: str) -> None:
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario: str) -> str:
        if entrada_do_usuario is None or entrada_do_usuario.strip() == '':
            raise Exception('String é obrigatória')

        return str(entrada_do_usuario)


class ConversorDeInputStringSOuN(ConversorDeInput):
    def __init__(self, texto_ao_usuario: str) -> None:
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario: str) -> str:
        entrada_minuscula = entrada_do_usuario.lower()

        if entrada_minuscula == 's' or entrada_minuscula == 'n':
            return entrada_minuscula

        raise Exception('Valor inválido. Digite "s" para sim ou "n" para não.')


# Conversores é uma "factory" (padrão de projeto) de conversores de input
conversores: dict[str, [ConversorDeInput]] = {
    'int': ConversorDeInputInt,
    'float': ConversorDeInputFloat,
    'int_pos': ConversorDeInputIntPositivo,
    'float_pos': ConversorDeInputFloatPositivo,
    'str_obg': ConversorDeInputStringObrigatoria,
    'str_s_n': ConversorDeInputStringSOuN
}

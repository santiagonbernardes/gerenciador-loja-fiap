class ConversorDeInput:
    def __init__(self, texto_ao_usuario):
        self.texto_ao_usuario = texto_ao_usuario

    def converta(self) -> str | int | float:
        while True:
            try:
                entrada_do_usuario = input(self.texto_ao_usuario)
                return self.converta_para_o_tipo(entrada_do_usuario)
            except NotImplementedError as erro:
                raise erro
            except Exception:
                print('O dado que você digitou não é válido.')

    # Daqui pra baixo, tudo deveria ser privado ou protegido
    def converta_para_o_tipo(self, entrada_do_usuario):
        # Este método deve ser implementado pelas classes filhas para que o método converta funcione
        raise NotImplementedError('Você está chamando a classe errada, corrija seu código')


class ConversorDeInputFloat(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario) -> float:
        return float(entrada_do_usuario)


class ConversorDeInputInt(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario) -> int:
        return int(entrada_do_usuario)


class ConversorDeInputIntPositivo(ConversorDeInputInt):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario) -> int:
        valor_convertido = int(entrada_do_usuario)
        if valor_convertido < 1:
            raise Exception('Valor não é positivo')

        return valor_convertido


class ConversorDeInputFloatPositivo(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario) -> float:
        valor_convertido = float(entrada_do_usuario)
        if valor_convertido < 1:
            raise Exception('Valor não é positivo')

        return valor_convertido


class ConversorDeInputStringObrigatoria(ConversorDeInput):
    def __init__(self, texto_ao_usuario):
        super().__init__(texto_ao_usuario)

    def converta_para_o_tipo(self, entrada_do_usuario) -> str:
        if entrada_do_usuario is None or entrada_do_usuario.strip() == '':
            raise Exception('String é obrigatória')

        return str(entrada_do_usuario)


# Conversores é uma "factory" (padrão de projeto) de conversores de input
conversores: dict[str, [ConversorDeInput]] = {
    'int': ConversorDeInputInt,
    'float': ConversorDeInputFloat,
    'int_pos': ConversorDeInputIntPositivo,
    'float_pos': ConversorDeInputFloatPositivo,
    'str_obg': ConversorDeInputStringObrigatoria
}

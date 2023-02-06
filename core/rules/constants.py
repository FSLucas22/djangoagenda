from enum import IntEnum, auto


PARA_SEMPRE = -1


class TipoRepeticao(IntEnum):
    TODA_HORA = auto()
    TODO_DIA = auto()
    TODA_SEMANA = auto()
    TODO_MES = auto()
    TODO_ANO = auto()
    TODO_DIA_UTIL = auto()
    A_CADA_PERIODO = auto()

    @classmethod
    @property
    def choices(cls):
        return [(key, key.value) for key in cls]

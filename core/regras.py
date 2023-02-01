from enum import IntEnum, auto


class TipoRepeticao(IntEnum):
    TODO_DIA = auto()
    TODA_SEMANA = auto()
    TODO_ANO = auto()
    TODO_DIA_DE_SEMANA = auto()
    A_CADA_PERIODO = auto()

    @classmethod
    @property
    def choices(cls):
        return [(key, key.value) for key in cls]

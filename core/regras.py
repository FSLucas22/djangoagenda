from enum import IntEnum, auto


PARA_SEMPRE = -1


class TipoRepeticao(IntEnum):
    NAO_REPETE = auto()
    TODO_DIA = auto()
    TODA_SEMANA = auto()
    TODO_ANO = auto()
    TODO_DIA_DE_SEMANA = auto()
    TODO_PERIODO = auto()

    @classmethod
    @property
    def choices(cls):
        return [(key, key.value) for key in cls]

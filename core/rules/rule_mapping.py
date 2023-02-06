from datetime import datetime
from typing import Callable
from core.rules import constants as c
from core.rules.constants import TipoRepeticao
import core.rules.repetition as r


RegraCallable = Callable[[datetime, ...], datetime]


_REGRAS: dict[c.TipoRepeticao, RegraCallable] = {
    TipoRepeticao.TODA_HORA: r.toda_hora,
    TipoRepeticao.A_CADA_PERIODO: r.a_cada_periodo,
    TipoRepeticao.TODO_DIA: r.todo_dia,
    TipoRepeticao.TODO_DIA_UTIL: r.todo_dia_util,
    TipoRepeticao.TODA_SEMANA: r.toda_semana,
    TipoRepeticao.TODO_MES: r.todo_mes,
    TipoRepeticao.TODO_ANO: r.todo_ano
}


def pega_regra_repeticao(tipo: c.TipoRepeticao) -> RegraCallable:
    return _REGRAS[tipo]

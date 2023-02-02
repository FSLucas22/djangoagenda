from datetime import datetime, timedelta
from calendar import monthrange, isleap


def a_cada_periodo(data_evento: datetime, periodo: timedelta, *args) -> datetime:
    return data_evento + periodo


def todo_dia(data_evento: datetime, *args) -> datetime:
    return a_cada_periodo(data_evento, timedelta(days=1))


def toda_semana(data_evento: datetime, *args) -> datetime:
    return a_cada_periodo(data_evento, timedelta(weeks=1))


def todo_mes(data_evento: datetime, *args) -> datetime:
    dias_no_mes = monthrange(data_evento.year, data_evento.month)[1]
    return a_cada_periodo(data_evento, timedelta(days=dias_no_mes))


def todo_dia_util(data_evento: datetime, *args) -> datetime:
    SABADO = 5
    SEXTA = 4
    dias_especiais = {SEXTA: 3, SABADO: 2}

    dia_semana_atual = data_evento.weekday()

    # se o dia da semana atual não for sexta ou sabado, então retorna 1
    dias_proximo_dia_util = dias_especiais.get(dia_semana_atual, 1)
    return a_cada_periodo(data_evento, timedelta(days=dias_proximo_dia_util))


def todo_ano(data_evento: datetime, *args, fevereiro_29: bool = False, ir_para_marco: bool = False) -> datetime:
    dia, mes, ano = data_evento.day, data_evento.month, data_evento.year
    if fevereiro_29:
        if isleap(ano+1):
            dia = 29
            mes = 2
        elif ir_para_marco:
            dia = 1
            mes = 3
        else:
            dia = 28
            mes = 2
    return datetime(ano+1, mes, dia, data_evento.hour, data_evento.minute)

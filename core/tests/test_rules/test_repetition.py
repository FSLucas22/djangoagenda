from datetime import timedelta, datetime

import core.rules.repetition as repetition
import pytest


@pytest.fixture
def uma_hora() -> timedelta:
    return timedelta(hours=1)

@pytest.fixture
def uma_hora_e_meia() -> timedelta:
    return timedelta(minutes=30, hours=1)


@pytest.fixture
def dois_dias() -> timedelta:
    return timedelta(days=2)


@pytest.fixture
def now() -> datetime:
    return datetime(year=2023, month=1, day=1, hour=23, minute=50)


@pytest.fixture
def segunda() -> datetime:
    return datetime(2023, 2, 6)


@pytest.fixture
def terca() -> datetime:
    return datetime(2023, 2, 7)


@pytest.fixture
def sabado() -> datetime:
    return datetime(2023, 2, 4)


@pytest.fixture
def domingo() -> datetime:
    return datetime(2023, 2, 5)


@pytest.fixture
def sexta() -> datetime:
    return datetime(2023, 2, 3)


@pytest.fixture
def ano_bissexto() -> datetime:
    return datetime(2024, 2, 29)


def test_a_cada_periodo(now: datetime, uma_hora: timedelta,
                        uma_hora_e_meia: timedelta, dois_dias: timedelta) -> None:
    assert repetition.a_cada_periodo(now, uma_hora) == datetime(2023, 1, 2, 0, 50)
    assert repetition.a_cada_periodo(now, uma_hora_e_meia) == datetime(2023, 1, 2, 1, 20)
    assert repetition.a_cada_periodo(now, dois_dias) == datetime(2023, 1, 3, 23, 50)


def test_todo_dia(now: datetime) -> None:
    assert repetition.todo_dia(now) == datetime(2023, 1, 2, 23, 50)


def test_toda_semana(now: datetime) -> None:
    assert repetition.toda_semana(now) == datetime(2023, 1, 8, 23, 50)


def test_todo_mes(now: datetime) -> None:
    assert repetition.todo_mes(now) == datetime(2023, 2, 1, 23, 50)


def test_todo_mes_funciona_em_fevereiro() -> None:
    assert repetition.todo_mes(datetime(2023, 2, 4)) == datetime(2023, 3, 4)


def test_todo_dia_util(segunda: datetime, terca: datetime) -> None:
    assert repetition.todo_dia_util(segunda) == terca


def test_todo_dia_util_funciona_na_sexta(sexta: datetime, segunda: datetime) -> None:
    assert repetition.todo_dia_util(sexta) == segunda


def test_todo_dia_util_funciona_no_sabado(sabado: datetime, segunda: datetime) -> None:
    assert repetition.todo_dia_util(sabado) == segunda


def test_todo_dia_util_funciona_no_domingo(domingo: datetime, segunda: datetime) -> None:
    assert repetition.todo_dia_util(domingo) == segunda


def test_todo_ano(now: datetime) -> None:
    assert repetition.todo_ano(now) == datetime(now.year+1, now.month, now.day, now.hour, now.minute)


def test_todo_ano_funciona_em_ano_bissexto(ano_bissexto: datetime) -> None:
    assert repetition.todo_ano(ano_bissexto, fevereiro_29=True) == datetime(2025, 2, 28)
    assert repetition.todo_ano(ano_bissexto, fevereiro_29=True, ir_para_marco=True) == datetime(2025, 3, 1)


def test_ano_anterior_ao_bissexto_vai_para_29_de_fevereiro_quando_flag_fevereiro_29_true(ano_bissexto) -> None:
    ano_anterior_em_fevereiro = datetime(2023, 2, 28)
    ano_anterior_em_marco = datetime(2023, 3, 1)
    assert repetition.todo_ano(ano_anterior_em_fevereiro, fevereiro_29=True) == ano_bissexto
    assert repetition.todo_ano(ano_anterior_em_marco, fevereiro_29=True) == ano_bissexto
    assert repetition.todo_ano(ano_anterior_em_fevereiro, fevereiro_29=True, ir_para_marco=True)

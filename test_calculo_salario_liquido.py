import pytest
from calculo_salario_liquido import calculo_salario_liquido


def test_um_calculo_salario_liquido():
    assert calculo_salario_liquido(
        6.25, 160, 1.3) == pytest.approx(987.00, 0.01)


def test_dois_calculo_salario_liquido():
    assert calculo_salario_liquido(
        20.5, 240, 1.7) == pytest.approx(4836.36, 0.01)


def test_tres_calculo_salario_liquido():
    assert calculo_salario_liquido(
        13.9, 200, 6.48) == pytest.approx(2599.86, 0.01)

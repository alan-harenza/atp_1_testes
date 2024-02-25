import pytest
from calculo_valor_promocao import valor_promocao


def test_um_valor_promocao():
    assert valor_promocao(500.00, 50.00) == pytest.approx(450.00, 0.01)


def test_dois_valor_promocao():
    assert valor_promocao(10500.00, 500.00) == pytest.approx(10000.00, 0.01)


def test_tres_valor_promocao():
    assert valor_promocao(90.00, 0.80) == pytest.approx(89.20, 0.01)

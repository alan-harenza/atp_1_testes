import pytest
from calculo_novo_valor_produto import novo_valor_produto


def test_um_calculo_novo_valor_produto():
    assert novo_valor_produto(100) == pytest.approx((91.00, 9.00), 0.01)


def test_dois_calculo_novo_valor_produto():
    assert novo_valor_produto(1500) == pytest.approx((1365.00, 135.00), 0.01)


def test_tres_calculo_novo_valor_produto():
    assert novo_valor_produto(60000) == pytest.approx(
        (54600.00, 5400.00), 0.01)

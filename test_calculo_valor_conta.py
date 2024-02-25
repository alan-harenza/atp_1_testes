import pytest
from calculo_valor_conta import valor_final_conta


def test_um_calculo_valor_conta():
    assert valor_final_conta(75.00) == pytest.approx((82.50, 7.50), 0.01)


def test_dois_calculo_valor_conta():
    assert valor_final_conta(125) == pytest.approx((137.50, 12.50), 0.01)


def test_tres_calculo_valor_conta():
    assert valor_final_conta(350.87) == pytest.approx((385.96, 35.09), 0.01)

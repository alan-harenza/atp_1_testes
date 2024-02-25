"""
função valor_final_conta()
entradas: valor_despesa:
saídas: valor_total_conta, valor_gorjeta

tipo variável: valor_despesa - float, int
"""


def valor_final_conta(valor_despesa):
    if isinstance(valor_despesa, (float, int)):
        valor_gorjeta = valor_despesa * 0.10
        valor_total_conta = valor_despesa + valor_gorjeta
        return valor_total_conta, valor_gorjeta

    else:
        raise TypeError

"""
função novo_valor_produto()
entradas: valor_produto
saídas: novo_valor, valor_desconto

tipo variável:  valor produto - int ou float
"""


def novo_valor_produto(valor_produto):
    if isinstance(valor_produto, (int, float)):
        valor_desconto = valor_produto * (9/100)
        novo_valor_produto = valor_produto - valor_desconto
        return novo_valor_produto, valor_desconto

    else:
        raise TypeError

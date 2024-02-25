"""
função: valor_promocao()
entradas: valor_original, desconto
saídas: valor_na_promocao
tipo das variávei: valor original - float
                   desconto - float
"""


def valor_promocao(valor_original, desconto):
    if isinstance(valor_original, float) and isinstance(desconto, float):
        valor_na_promocao = valor_original - desconto
        return valor_na_promocao
    else:
        raise TypeError

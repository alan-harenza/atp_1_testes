"""
função calculo_inss()
entradas: valor_hora_aula, nro_aulas, percentual_inss
saídas: o valor  do salário liquido com o desconto do inss
Tipo de cada variável - valor_hora_aula - float
                      - nro_aulas - int
                      - percentual - float
"""


def calculo_salario_liquido(valor_hora_aula, nro_aulas, percentual_inss):
    salario_bruto = valor_hora_aula * nro_aulas
    salario_liquido = salario_bruto * (1 - (percentual_inss/100))
    return salario_liquido

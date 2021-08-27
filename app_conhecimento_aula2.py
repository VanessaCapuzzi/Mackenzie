# Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar:
# a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.
# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.

import math

custo = float(input())
convite = float(input())
quantidade = (custo/convite)
lucro = ((custo*1.23)/convite)
print(math.ceil(quantidade))
print(math.ceil(lucro))

#  Faça um programa que mostre os números pares entre 1 e 100, inclusive.
# Feito
"""
x = 0

while x < 101:
    x += 1
    if x % 2 == 0:
        print(x)
"""
# Com for
limites = range(1, 101)
for numeros in limites:
    if numeros % 2 == 0:
        print(numeros)
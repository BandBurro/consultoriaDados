# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
# Feito
"""
nuser = input()
nuser = int(nuser)
x = 1
y = 10000
z = 3

while x < y:
    x += 1
    if x % nuser == 2:
        print(x)
"""
# Com for
n = input()
entre = range(1, 10001)
for numero in entre:
    n = int(n)
    if numero % n == 2:
        print(numero)



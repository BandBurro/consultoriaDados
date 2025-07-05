"""
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
"""
# Feito
"""
n = input()
n = int(n)

if n % 2 == 0:
    quadradodopar = n ** 2
    print(quadradodopar)
    while 1 <= n:
        n -= 1
        if n % 2 == 0:
            quadradodopar = n ** 2
            print(quadradodopar)
"""
"""
n = input()
n = int(n)

while 5 < n < 2000:
    n -= 1
    if n % 2 == 0:
        quadradodopar = n ** 2
        print(quadradodopar)
"""
# Com for
n = input()
iterador = range(1, 2001)
for numero in iterador:
    n = int(n)
    if numero == (n + 1):
        break
    if numero % 2 == 0:
        quadrado = numero ** 2
        print(quadrado)









"""
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:
1 x N = N      2 x N = 2N        ...       10 x N = 10N
"""
# Feito
"""
n = input()
n = int(n)
acumulador = 0
stopper = 0

while 2 < n < 1000:
    acumulador += 1
    stopper += 1
    tabuada = acumulador * n
    print(tabuada)
    if stopper == 11:
        break
"""
# Com for
n = input()
iterador = range(11)
for numero in iterador:
    n = int(n)
    iterador = int(n)
    result = n * numero
    print(result)









"""
Leia um valor inteiro X.
Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.
"""
# Feito
"""
x = input()
acumulador = 0

if x.isnumeric():
    x = int(x)
    while x < 100000:
        if x % 2 != 0:
            print(x)
            acumulador += 1
        x += 1
        if acumulador == 6:
            break
"""
# Com for é embaçado pq preciso de um limite de range
"""
n = input()
iterador = range(1, 7)
for numero in iterador:
    n = int(n)
    if n % 2 != 0:
        print(n)
"""
# Da pra fazer sem limites com o while
"""
n = input()
stopper = 0
while True:
    n = int(n)
    if n % 2 != 0:
        print(n)
        n += 1
        continue
    else:
        n += 1
        continue
"""
n = int(input())

if n % 2 == 0:
  n += 1
for i in range(6):
  print(n)
  n += 2






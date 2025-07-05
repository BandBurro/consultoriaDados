# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
# Feito
"""
x = input('Um valor inteiro: ')
y = input('Outro valor inteiro: ')
acumuladora = 0

if x.isnumeric() and y:
    x = int(x)
    y = int(y)

    while x < y:  # Iterar todos os numeros entre X e Y
        x += 1
        if x % 2 != 0:  # Numero impar é o numero que divido por 2 da resto DIFERENTE (!=) de 0
            acumuladora += x
    print(acumuladora)
"""
"""
padaria > passa o produto um por um no scanner > cada uma das escaneadas da o valor de UM produto > quanto foi o total da conta
> para encerrar a execução do codigo vou passar o valor 0 > ao passar o valor 0, printa o valor TOTAL
"""

"""
if x.isnumeric() and y.isnumeric():
    while x < y:
        x = int(x)
        y = int(y)
    else:
        break
        
        while x != y:
            x += 1
            print(x)

elif x.isnumeric() and y.isnumeric():
    while x > y:
        x = int(x)
        y = int(y)
        while y != x:
            y += 1
            print(y, 'asd')
    else:
        break
"""
# Com for
while True:
    x = input()
    y = input()
    x = int(x)
    y = int(y)
    l1 = []
    limite = range(x, (y + 1))
    if x > y:
        print('Digite um valor X, em seguida um maior que X')
        continue
    else:  # Pq o ELIF aqui nao funciona?
        limite = range(x, (y + 1))
        for numeros in limite:
            limite = range(x, (y + 1))
            x = int(x)
            y = int(y)
            int(numeros)
            if numeros % 2 != 0:
                l1.append(numeros)
    print(sum(l1))


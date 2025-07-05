"""
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.
"""
qntd = input('Numero de contas ')
qntd = int(qntd)

for i in range(qntd):
    user1 = input('Numero 1 ')
    user2 = input('Numero 2 ')
    user2 = int(user2)
    user1 = int(user1)
    if user2 == 0:
        print('Divisao impossivel')
    else:
        print(user1/user2)

























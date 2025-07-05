'''
Operadores relacionais, me retornam valores booleanos, portantao, sao perguntas
== igualdade
> maior que
>= maior que ou igual
< menor que
<= menor que ou igual
!= diferente
'''
print(2 == 2)  # ao usar os dois ==, significa que estou PERGUNTANDO se ambos sao realmente iguais, ao usar apenas um
# =, eu estou ATRIBUINDO um valor a outro, tipo nas variaveis nome = X, idade = Y
print(2 == 1)
num_1 = 2
num_2 = '2'
print(num_1 == num_2)  # Essa expressao é falsa por comparo uma str com um int, apesar dos valores serem iguais
expressão = num_1 == num_2
print(expressão)
print(2 > 1)
print(2 > 3)
print(2 > 2)
print(2 >= 2)
print(2 != 3)
print(2 != 2)
print('Luiz' != 'Luis')
print('Luiz' != 'Luiz')

idade = int(input())
if idade > 18:
    print('Emprestimo concedido')

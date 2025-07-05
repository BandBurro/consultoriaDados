"""
Leia a documentação da linguagem ou do framework que vc usa:
https://docs.python.org/3/library/stdtypes.html
https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
Esse link do github sao funções construidas pelo proprio professor com variantes de funções do python,
elas vao checar
"""

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

"""
essas funções checam se a str pode ser convertida em um numero inteiro
retornam um booleano que me diz se podem ser convertidos ou nao
isnumeric: retorna true se todos os caracteres da str numeros positivos
isdigit: retorna true se todos os caracteres da str forem numeros e tiver pelo menos um caracter (segunda parte tem que ter algo)
isdecimal: retorna true se todos os caracteres da str forem decimais
e o ultimo recurso é o https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
"""

print(num1.isnumeric())
print(num2.isnumeric())
if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
    print('Por retornarem valores booleanos, retorna uma conclusao para meu If')

"""
elif num1.isdigit() or num2.isdigit():
    print('fodase') #  Esta expressao esta condicionada a apenas UM digito errado no input
else:
    print('Voce digitou DOIS caracterer invalido')

O python nunca vai assumir valores e "considerar que algo pode ser outra coisa" alem do expressamente escrito
como por exemplo, so vai considerar a str do input um int se eu expressamente dizer que deve
-
O objetivo do dev é evitar o erro antes dele acontecer, como por exemplo, caso o usuario digite uma letra e o python
tente converte-la para int, o que crashara o .exe, por essa razao, inclusive, recomenda-se nao colocar o int direto 
no input, tipo assim: num1 = int(input('Digite um numero: '))
-
try:
except:
tente esse codigo, caso tenha qualquer erro ou execução, vc executa esse outro bloco de codigo, mas nao apresenta o erro na tela
"""



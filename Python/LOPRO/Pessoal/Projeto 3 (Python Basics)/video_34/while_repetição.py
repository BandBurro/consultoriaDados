"""
Utilizada para realizar ações enquanto uma condição for V
while
for

a)
while True:  !loop infinito enquanto a condição for V!
    nome = input('Qual seu nome? ')
    print(f'Ola {nome}!')
print('Não sera executada)

O while vai checar se a sua condição for verdadeira (no caso, o while esta EXPLICITAMENTE com true), caso seja V, ela executara
o bloco de codigo filho e depois checara NOVAMENTE a condição, que, continuara sendo V, portanto, loopando infinitos.
No caso acima, inclusive, o ultimo print NUNCA sera executado pois a condição do while é V pra sempre
"""
"""
x = 0
while x < 100:
    print(x)
    x = x + 1
print("Acabou")
"""
"""
Neste codigo, eu digo ao interpretador que X é 0 e dou a operação a ser executada, como o X é de fato menor que 0, o programa
considera como V e executa a operação, sendo assim, soma um a X, o importante desta operação é para onde o PC volta!
O PC volta à linha 18 e nao à 17, portanto, o X tera um novo valor, sendo este, 1.
"""
"""
y = 0
while y < 10:
    if y == 3:
        y = y + 1
        continue
    print(y)
    y = y + 1
print("Acabou")
"""
"""
O continue serve para pular o proximo bloco de comando e voltar ao while, no caso, quero que pule o nomero 3, executando sem o continue
o codigo contara ate o 10 sem problemas. Ou seja, continua o loop infinitamente, o terminal do pycharm fica rodando
pra sempre, lembrar de parar o execute!
"""
"""
z = 0
while z < 10:
    if z == 3:
        z = z + 1
        break
    print(z)
    z = z + 1
print("Acabou")
"""
"""
O break é muito similar ao continue, quando o interpretador le ele, ele para de executar o codigo e pula para O FINAL
ao inves de VOLTAR AO WHILE (a diferença entre break e continue)
"""
"""
x = 0  # Coluna
while x < 10:
    y = 0  # Linha
    while y <= 5:
        print(f'({x},{y})')
        y += 1
    x += 1  # x = x + 1
"""
"""
Neste codigo, o while dentro do while executa a sua conta ate chegar no 5, quando chega no 5 ele vira falso, executa a linha
64, e volta pra 59, pois a condiçao dela é 10, e a primeira volta deixa ele apenas no 1, entao, a cada 5 do Y soma 1 do X
"""

while True:
    print()
    num1 = input('Digite um numero ')
    num2 = input('Digite outro numero ')
    operator = input('Digite um operador ')  # + - / *

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um numero e um operador ou sair ')
        sair = input('Deseja sair? s ou n ')
        if sair == 's':
            print('Adeus')
            break
        elif sair == 'n':
            continue
    else:
        num1 = int(num1)
        num2 = int(num2)

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '/':
        print(num1 / num2)
    elif operator == '*':
        print(num1 * num2)
    else:
        print('Operador Invalido ')
        sair = input('Deseja sair? s ou n ')
        if sair == 's':
            print('Adeus')
            break
        elif sair == 'n':
            continue

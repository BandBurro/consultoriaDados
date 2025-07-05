'''
Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral.
O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código
(1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução de
todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

Entrada
O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas, deve
ser lido um valor inteiro X . O programa deve parar quando o valor lido para este X for igual a 2.

Saída
Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas,
deve ser impressa a mensagem “media = ” seguido do valor do cálculo.

Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem deve ser apresentada
novamente se o valor da entrada padrão para X for menor do que 1 ou maior do que 2, conforme o exemplo abaixo.

A média deve ser impressa com dois dígitos após o ponto decimal.
'''
"""
while True:
    nota1 = int(input('Primeira Nota '))
    nota2 = int(input('Segunda Nota '))
    verifnota1 = nota1 < 0 or nota1 > 10
    verifnota2 = nota2 < 0 or nota2 > 10
    while verifnota1:
        print('Primeira Nota Invalida')
        nota1 = int(input('Digite uma nota valida '))
        verifnota1 = nota1 < 0 or nota1 > 10
    while verifnota2:
        print('Segunda Nota Invalida')
        nota2 = int(input('Digite uma nota valida '))
        verifnota2 = nota2 < 0 or nota2 > 10
    else:
        print(f'Media = {(nota1+nota2)/2}')
    repeat = input('Digite 1 para continuar, e 2 para sair ')
    while repeat != '1' and repeat != '2':
        repeat = input('Digite 1 para continuar, e 2 para sair ')
        continue
    else:
        if repeat == '1':
            continue
        elif repeat == '2':
            exit(0)
"""

notas = []
escolha = -1
while escolha != 2:
    while len(notas) < 2:
        nota = float(input())
        if nota > 0 and nota < 10:
            notas.append(nota)
        else:
            print("Nota inválida!")
        if len(notas) == 2:
            print("Media:", sum(notas) / 2)
    print("Digite 1 para continuar, e 2 para sair")
    escolha = int(input())
    if escolha == 1:
        notas = []

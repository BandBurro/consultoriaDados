"""
Keanu estava testando novos modelos de tabuleiros de xadrez quanto teve a seguinte duvida:

Quantas casas brancas e quantas casas pretas tem um tabuleiro de xadrez de tamanho nxn?

Observe que a casa mais acima e mais à esquerda é sempre branca.

Entrada
O input consiste de uma linha com um único inteiro n.

2 ≤ n ≤ 100

Saída
Imprima "a casas brancas e b casas pretas" sem aspas, sendo a a quantidade de casas brancas e b a quantidade de casas pretas.
"""
while True:
    casas = input('Seu tabulero será de n por n, digite um valor inteiro >= 2 e =< 100: ')
    if casas.isdigit():
        casas = int(casas)
        if casas <= 1 or casas >= 100:
            print('Insira um número VÁLIDO')
            continue
        elif 2 <= casas <= 100:
            tabuleiro = casas * casas
            if tabuleiro % 2 == 0:
                print(f'Seu tabuleiro tem {int(tabuleiro / 2)} casas brancas e {int(tabuleiro / 2)} casas pretas')
            elif tabuleiro % 2 != 0:
                print(
                    f'Seu tabuleiro tem {int((tabuleiro / 2) + 1)} casas brancas e {int(tabuleiro / 2)} casas pretas ')
    else:
        print('Digite um NÚMERO')
        continue
























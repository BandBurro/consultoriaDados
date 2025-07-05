"""
Como se sabe, léxico é o conjunto de palavras que existe em uma língua. Nas línguas ocidentais, é comum escrever usando
o alfabeto latino, com 26 letras que vão de a até z.

É comum enumerar as letras na seguinte ordem: a, b, c, d, e f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z.

Se uma lista de palavras está organizadas de acordo com esta ordem, fica muito mais rápido pesquisá-las. Seu trabalho
neste problema é ordenar duas palavras de acordo com esta ordem.

Sejam duas palavras A e B. Caso o primeiro caractere de A venha antes do primeiro de B, coloca-se A antes de B. Se o
primeiro caractere for igual, usa-se o seguinte para desempate.

E se o segundo empatar, usa-se o terceiro, etc. Quando todos os caracteres de A forem iguais ao começo de B, ou todos os
de B forem iguais ao começo de A, coloca-se a menor palavra primeiro.

Entrada
A entrada contém 2 palavras com caracteres minúsculos de a até z, O comprimento das palavras não ultrapassa 20 caracteres.

Saída
A saída contém as mesmas 2 palavras, só que na ordem lexicográfica.
"""
"""
a = input()
b = input()

if a < b:
    print(a)
else:
    print(b)
"""
"""
lexa = list(input())
lexb = list(input())

for i in range(lexa, lexb):
    if lexa[i] > lexb[i]:
        print(lexb)
    elif lexa[i] < lexb[i]:
        print(lexa)
    else:
        continue
"""
"""
lexa = input()
lexb = input()

for i in range(max(len(lexa), len(lexb))):
    if lexa == lexb:
        print(lexa, lexb)
        break
    elif i == len(lexa):
        print(lexa, lexb)
        break
    elif i == len(lexb):
        print(lexb, lexa)
        break
    elif lexa[i] > lexb[i]:
        print(lexb, lexa)
        break
    elif lexa[i] < lexb[i]:
        print(lexa, lexb)
        break
    else:
        continue
"""

lexa = input()
lexb = input()

for i in range(min(len(lexa), len(lexb))):
    if lexa == lexb:
        print(lexa, lexb)
        break
    elif lexa[i] > lexb[i]:
        print(lexb, lexa)
        break
    elif lexa[i] < lexb[i]:
        print(lexa, lexb)
        break
    elif i == (len(lexa)-1):
        print(lexa, lexb)
        break
    elif i == (len(lexb)-1):
        print(lexb, lexa)
    else:
        continue
"""       
    elif i == len(lexa):
        print(lexa, lexb)
        break
    elif i == len(lexb):
        print(lexb, lexa)
        break
    elif lexa[i] > lexb[i]:
        print(lexb, lexa)
        break
    elif lexa[i] < lexb[i]:
        print(lexa, lexb)
        break
    else:
        continue
"""
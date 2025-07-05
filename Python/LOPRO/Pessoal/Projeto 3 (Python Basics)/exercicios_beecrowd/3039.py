"""
Papai Noel todo ano lê as cartinhas de Natal para saber o que dar de presente para cada criança.
O problema é que muitas crianças não mandam suas cartinhas para o Papai Noel.
Então ele decidiu que, para poupar o seu tempo, ele irá dar o mesmo presente para crianças que não mandaram cartinhas.
Assim, ele decidiu que para os meninos ele irá dar um carrinho de brinquedo e para as meninas, uma boneca.

Entrada
A primeira linha da entrada possui um inteiro N (0 < N ≤ 1000), o número de crianças que não enviaram sua cartinha para o Papai Noel.
As próximas N linhas consistem em duas strings, a primeira é o nome da criança, e a segunda é uma letra, que pode ser ‘M’, para dizer que é um menino, ou ‘F’ se for uma menina.

Saída
A saída consiste em 2 linhas.
A primeira linha deve conter o número de carrinhos que o papai noel deve fazer, seguido pela palavra “carrinhos”,
e na segunda linha, o número de bonecas seguido pela palavra “bonecas”.
"""
"""
loop = 0
listamaior = []
listaf = []
listah = []
listanome = []
while True:
    nmandou = input('Número de 1 a 1000 de crianças que não mandaram: ')
    nmandou = int(nmandou)
    if nmandou < 1 or nmandou > 1000:
        print('Digite um numero válido (1 a 1000): ')
        continue
    while loop < nmandou:
        loop += 1
        nome = input('Digite seu Nome: ')
        listanome.append(nome)
        listamaior.append(listanome)
        gen = input('Digite seu gênero (H ou F): ')
        while gen.upper() != 'F' and gen.upper() != 'H':
            print('Digite uma das duas opções de gênero: ')
            gen = input('Digite seu gênero (H ou F): ')
            if gen == 'F':
                listaf.append(gen)
            elif gen == 'H':
                listah.append(gen)
            continue
        if gen.upper() == 'F':
            listaf.append(gen.upper())
        elif gen.upper() == 'H':
            listah.append(gen.upper())
        listamaior.append(listah)
        listamaior.append(listaf)
    if nmandou == loop:
        for generoh in listah:
            vezesh = listah.count(generoh)
            totalh = vezesh
        print('O numero de carrinhos é', totalh)
        for generof in listaf:
            vezesf = listaf.count(generof)
            totalf = vezesf
        print(f'O numero de numero de bonecas é {totalf}')

print('O numero de carrinhos é', totalh)
print(f'O numero de numero de bonecas é {totalf}')

#  Nao sei pq mas se eu apagar o print de dentro do loop for, as variaveis totais fora do loop while sao afetadas
"""
n = int(input())

num_carrinhos = 0
num_bonecas = 0
for i in range(n):
    if input().split(" ")[1] == "F":
        num_bonecas += 1
    else:
        num_carrinhos += 1

print(f"{num_carrinhos} carrinhos")
print(f"{num_bonecas} bonecas")
























'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e
calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =

O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto
flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''

x2x1 = ((5.0 - 1.0) ** 2)
y2y1 = ((9.0 - 7.0) ** 2)

soma_predistancia1 = x2x1 + y2y1
distancia1 = soma_predistancia1 ** (1/2)
print(f'{distancia1:.4f}')

eex2 = ((12.1 - (-2.5)) ** 2)
eey2 = ((7.3 - 0.4) ** 2)
soma_predistancia2 = eex2 + eey2
distancia2 = soma_predistancia2 ** (1/2)
print(f'{distancia2:.4f}')

eex3 = (((-12.2) - 2.5) ** 2)
eey3 = ((7.0 - (-0.4)) ** 2)
soma_predistancia3 = eex3 + eey3
distancia3 = soma_predistancia3 ** (1/2)
print(f'{distancia3:.4f}')

# Sou burro e nao sei fazer raiz quadrada no python


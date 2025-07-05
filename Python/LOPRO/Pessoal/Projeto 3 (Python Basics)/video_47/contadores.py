"""
for/while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
contador2 = 10
for i in range(9):
    print(i, contador2)
    contador2 -= 1
print()
#for ii in range(8):
    #contador2 -= 1
for p, r in enumerate(range(10, 1, -1)):  # o contador do R (o regressivo) é feito pelo range com o -1 no final, e o enumerate, apenas enumera cada volta do laço que coincidira com os negativo
    print(p, r)
"""
Lembrando que o range o primeiro valor é o start, o segundo é o ending e o terceiro é o step, que pode ser positivo ou negativo (caso negativo, será feito ao contrario)
"""













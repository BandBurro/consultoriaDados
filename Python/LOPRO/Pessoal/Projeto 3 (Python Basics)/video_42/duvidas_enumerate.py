"""
Enumerate e seus detalhes
"""
#          0       1       2
lista = ['Edu', 'Joao', 'Luiz']

# Numa lista posso ter várias listas
#            0       1       2
lista2 = [['Edu', 'Joao', 'Luiz'],  # Este é o indice 1
          ['Maria', 'Aline', 'Joana'],  # Este é o indice 2
          ['Helena', 'Ed', 'Lu']]  # Este é o indice 3
"""
Caso eu queira pegar um termo especifico da lista, pego o indice da lista que representa o bloco de lista em que
tem o termo que estou mirando, no caso "Joana", que esta no indice 1 da lista grande, e, em seguida, o indice 2 da lista
pequena, no caso, a lista que tem Maria, Aline e Joana.
Portanto, ficaria assim
"""
print(lista2[1][2])
print()
enumerada = list(enumerate(lista2))
print(enumerada)  # Esse enumerada me volta um objeto enumerate (range tbm) me volta um objetivo ITERAVEL, portanto, posso fazer um typecast para um list
print(list(enumerada))
print(enumerada[1][1])
print()
"""

[  <---- Enumerate
     0  1 
    (0, ['Edu', 'Joao', 'Luiz']), # 1 
           0       1       2
    (1, ['Maria', 'Aline', 'Joana']), # 2
    (2, ['Helena', 'Ed', 'Lu']) # 3
]
"""
for v1 in enumerate(lista2):
    valor_enumerodo, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3
          )






'''
Desempacotamento

'''

lista = ['Fodase', 'Demais', 'Prakrl']
n1, n2, n3 = lista  # Isto é desempacotar
print(n1, n2, n3)
print()
"""
n1, n2 = lista  
Este codigo da erro, nao posso tentar desempacotar uma lista com um numero menor de variaveis do que tem na lista
ValueError, too many values to unpack
Mas eu posso tentar desempacotar dois valores de uma lista e juntar todo o resto em uma variavel com asterisco antes
que se chama outra lista, como no exemplo abaixo
"""

lista2 = ['Fodase', 'Demais', 'Prakrl', 1, 2, 3, 4, 5, 6]
n1, n2, *outra_lista = lista2  # Coloquei n1 e n2 mas posso colocar o que eu quiser
print(n1, n2, n3, outra_lista)  # Note que eu posso, inclusive, printar o terceiro indice da lista sem ter uma variavel hardcoded dela, mas, como ela esta englobado na variavel outra_lista, o n3 vai aparecer duas vezs
"""
Tudo que for colocado em variavel depois do outra lista, vai pegando do final da lista do ultimo em direção ao primeiro valor, como no caso abaixo
"""

lista3 = ['Fodase', 'Demais', 'Prakrl', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
n1, n2, *outra_lista2, penultimo, ultimo = lista3
print(n1, n2, n3, penultimo, ultimo)
print(outra_lista2)  # Este print vai me dar os valores que nao estao determinados com variavel dentro da lista, ou seja, tudo do 1 ate o 12























"""
+
-
*
/ divisao exata
// divisao com numero inteiro (arrendodada)
** exponenciação ou potencia
% resto da divisao entre numeros
() alterar a precedencia nas contas
"""
print('Multiplicação * ', 10 * 10)
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 8)
print('Divisão / ', 10 / 2)
# Não é possivel usar multiplicação entre strings, ex print('Multiplicação * ', '10' * '10')
# É possivel utilizar o simbolo de multiplicação para repetir a string o numero de vezes que vc quiser
print('Multiplicação * ', 10 * '10')
print('Multiplicação * ', 10 * 'AB')
# É possivel usar a SOMA entre DOIS (so um nao rola) strings para COCATENAR (juntar)
print('Adição + ', '10' + '10')
print('Adição + ', 'Ele' + ' ' + 'Mrm')
# Essa divisao com duas barras arrendonda
print(10.5 // 3)
# A divisao com apenas uma barra me da o valor certo
print(10 / 3)
# Essa operação me da o resto da operação
print(10 % 3)
print(10 % 5)
# Exemplo de potenciação
print(10 ** 2)
# Caso use a precedeencia de parenteses a conta é feita na ordem dos fatores, ou seja, multiplicação primeiro e tals
print(5+2*10)  # Primeiro multiplica
print((5+2)*10)  # Primeiro parenteses
# Poliformismo é o quando um operador faz duas coisas diferentes, como o exemplo do * que tanto multiplica qnto repete as strings
'''
Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses (como descrito na aula anterior).
Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas (de maior para menor precedência).
1. ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro
2. ** - Depois vem a exponenciação
3. * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo
4. +  - - Por fim, soma e subtração
Contas com operadores de mesma precedência são realizadas da esquerda para a direita.
'''
print(2 + 5 * 3 ** 2 - (23.5 + 23.5))
print(3 ** 2)

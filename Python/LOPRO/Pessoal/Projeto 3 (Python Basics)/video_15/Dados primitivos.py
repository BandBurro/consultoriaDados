"""
Tipos de dados
str - strings: coisas que estao dentro de aspas simples ou duplas 'Assim' "Assim"
int - inteiro: 123456, numero negativo ou positivo (ou ate o 0), sem decimais
float - numero real/ponto flutuante: 1.1, 1.2, -1.3, -1.4... numeros decimais (sempre usa ponto para separar decimais)
bool - booleano/lógico: valores binarios entre V e F (10==10)
"""
print(                type('eu')                     )  # Comando type, ao ser runnado, me da a classe da funçao/comando
print(10, type(10))  # Caso runnado, vai me dar um int, de inteiro, mas, cuidado ao runnar com as aspas, pois caso o faça, vai me dar uma string
print(10, type('10'))  # Mas, cuidado ao runnar com as aspas, pois caso o faça, vai me dar uma string
print(25.23, type(25.23))  # Gerou um float
'''
Gerou um true, ao usar dois iguais, é como se perguntasse ao interpretador se 10 é igual a 10
Tambem é usavel com letras ou afins
'''
print(10 == 10, type(10 == 10))
print('L' == 'l', type('L' == 'l'))
print(bool('elemrm'))  # tambem posso usar o comando direto para me dar um falso ou true da existencia de algo, sem nada é falso, com algo é true
print('eu', type('eu'), bool('ele'))
# Tambem é possivel converter classes da seguinte maneira, o nome disse é type casting
print('10', type('10'), type(int('10')))
# Mas nao é possivel converter, por exemplo, um texto em um numero
print('eu', int('10'))  # basta runnar para ver o erro
# Mas é possivel converter em funçoes corretas, como float com numero ou int com numero inteiro
print('eu', int('10'))
print('eu', float('10'))
print(10 + 10, end=' ')
print('10' + '10')
# String: nome
print('Matheus', type('Matheus'))

# Int: idade
print('24', type(24))

# Float: altura, lembrar de usar o ponto como decimal e nao virgula
print('1.80', type(1.80))

# Bool: maioridade
# Usei o operador de igualdade, mas posso usar os > e < tambem
print(18 < 24, type(18 < 24))



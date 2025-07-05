"""
Regras de variaveis: 1- Iniciar com letra 2-  Separar coPode conter numeros 3-m _ 4- Letras minusculas
Variaveis meio que salvam algum comando na "memoria do pc", ou seja, vou dar o certo nome ao comando e ele será sempre
executado ao digitar "nome"
Operador de atribuiçao (essa é a palavra chave)
Ex: nome = Eu
print(nome)
"""
nome = "gfonhdopksadfhiujgds"  # Str
idade = 25  # Int
altura = 2.84  # Float
maioridade = 18 < idade  # Bool
peso = 80
data_1 = True  # Bool (neste caso é um valor booleano explícito, ja digido o valor em True ou False direto, começando com maisculo)
data_atual = 2019  # Int
imc = peso/(altura**2)

print(nome, type(nome), bool(nome))
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maioridade:', maioridade)
print('IMC:', peso/(altura**2))
'''
Tambem é possivel usar as variaveis com operadores aritmeticos, como, por exemplo, multiplicar dois operadores de atribuição
Tipo idade * altura
'''
print(idade * altura)
print(nome, 'tem', idade, 'de idade e seu IMC é', imc)
print(nome * idade)

'''
Criar variaveis para nome (str), idade (int), altura (float) e peso (int) de uma pessoa
Criar variavel com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando f-strings (com as chaves {})
'''
nome = 'Bilu'
idade = 25
altura = 1.80
peso = 80
ano_atual = 2022
nascimento = ano_atual - idade
IMC = peso/altura**2
print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}kg.')
print(f'o IMC de {nome} é {IMC:.3f}.')
print(f'{nome} nasceu em {nascimento}')
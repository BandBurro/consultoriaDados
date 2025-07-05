'''
Entrada de dados - Aula 3
Recebe uma string do usuario que precisemos
'''
# nome = input(f'Qual o seu nome? ')
# print(f'O usuario digitou {nome} e o tipo da variável é '
     # f'{type(nome)}')
nome = input(f'Qual o seu nome? ')  # Sempre coloque um espaço no final da frase para que a resposta do input não
# fique colada na interrogação nome = input(f'Qual o seu nome?') ERRADO nome = input(f'Qual o seu nome?' ) CERTO
idade = input(f'Qual a sua idade? ')
# ano_nascimento = 2022 - idade este comando nao funciona pois estou tentando subtrair um int de um str, portanto, devo fazer casting
ano_nascimento = 2022-int(idade)

print()  # Este print vazio pula uma linha entre a variavel "idade" e o print de resultado
print(f'{nome} tem {idade} anos. '
      f'{nome} asceu em {ano_nascimento}.')

print(f'Concessão de emprestimo para maiores de 18 anos')
nome = input(f'Qual o seu nome? ')
idade = int(input(f'Qual a sua idade? '))
idade_limite = 18
if idade >= idade_limite:
    print(f'Parabens {nome}. Seu emprestimo foi concedido')
else:
    print(f'Infelizmente {nome} nao tem a idade minima para requerir este serviço')
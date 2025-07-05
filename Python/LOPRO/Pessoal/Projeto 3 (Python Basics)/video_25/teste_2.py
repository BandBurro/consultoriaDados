
print(f'Concessão de emprestimo para maiores de 18 anos')
nome = input(f'Qual o seu nome? ')
idade = int(input(f'Qual a sua idade? '))
# Emprestimo apenas para > 20 e < 30
idade_min = 20
idade_max = 30
if idade_min <= idade <= idade_max:
    print(f'Parabens {nome}. Seu emprestimo foi concedido')
else:
    print(f'Infelizmente {nome} nao tem a idade requerida este serviço')
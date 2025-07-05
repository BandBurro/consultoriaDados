'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

O arquivo de entrada contém um valor inteiro.
Imprima a saída conforme exemplo fornecido.
'''

dias_user = input('Quantos dias de vida você tem? ')
anos_int = int(dias_user) // 365
print(f'Ano(s)', anos_int)
anos_rest = int(dias_user) % 365
meses_int = anos_rest // 30
print(f'Mês(es)', meses_int)
meses_rest = anos_rest % 30
print(f'Dia(s)', meses_rest)





"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

vbc-shqr-wxd (Meet)

- Problema anterior:
- Implemente o programa que leia o ano de nascimento de uma pessoa e calcule
sua idade. Verifique se ela já tem idade para votar (16 anos ou mais).
Mostre a mensagem informando a situação dela.

- Problema atual:
- Implemente o programa que leia o ano de nascimento de uma pessoa e calcule
sua idade. Verifique se ela já tem idade para votar (16 anos ou mais) e para
conseguir a CNH - Carteira Nacional de Habilitação (18 anos ou mais).
Mostre a mensagem informando a situação dela.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Cálculo (processamento)
Testes (se ...)
Saída de dados (escreva)

Teste 1: Entrada: Ano nascimento = 2010          Saída: Não votar, não CNH.
Teste 2: Entrada: Ano nascimento = 2008          Saída: Pode votar, não CNH.
Teste 3: Entrada: Ano nascimento = 2000          Saída: Pode votar, pode CNH.
"""
# Solução 1:
ano_nascimento = int(input("Ano de nascimento: "))
idade = 2025 - ano_nascimento
if idade >= 16:
    print("Pode votar.")
else:
    print("Não pode votar.")

if idade >= 18:
    print("Pode tirar CNH.")
else:
    print("Não pode tirar CNH.")
''' --- ALTERAÇÕES:
a. Refaça usando somente um teste: if ... elfi ... else
    --- DICAS:
'''
# Solução 2:
ano_nascimento = int(input("Ano de nascimento: "))
idade = 2025 - ano_nascimento
if idade >= 18:
    print("Pode tirar CNH e votar.")
elif idade >= 16 and idade < 18:
    print("Pode votar e não tem idade para tirar CNH.")
else:
    print("Não tem idade nem para votar nem para tirar CNH.")
''' --- ALTERAÇÕES:
a. Retire a redundância dos testes na solução 2      

'''

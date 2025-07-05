"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

vbc-shqr-wxd (Meet)

- Problema:

- Implemente o programa que leia o ano de nascimento de uma pessoa e calcule
sua idade. Verifique se ele já tem idade para votar (16 anos ou mais).
Mostre a mensagem informando a situação dela.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Cálculo (processamento)
Testes (se ...)
Saída de dados (escreva)

Teste 1: Entrada: Ano nascimento: 2010          Saída: Não pode votar.
Teste 2: Entrada: Ano nascimento: 2000          Saída: Pode votar.

"""

ano_nascimento = int(input("Ano de nascimento: "))

idade = 2025 - ano_nascimento

if idade >= 16:
    print("Pode votar.")

else:
    print("Não pode votar.")

''' --- ALTERAÇÕES:
a. Na tela de saída, mostre também a ano de nascimento.      
b. Na tela de saída, mostre também a idade da pessoa.
c. Na tela de saída, mostre tqmbém o nome da pessoa.
d. Refaça, pegando o ano atual usando biblioteca do Python. 

'''

"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.
vbc-shqr-wxd (Meet)

- Problema:
- Construa o programa que leia dois valores quaisquer e mostre o maior
deles ou mostre a mensagem “Os valores são iguais.”

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Testes (se ...)
Saída de dados (escreva)

Teste 1: Entrada: 5 e 10                    Saída: O maior valor é 10

Teste 2: Entrada: 10 e 5                    Saída: O maior valor é 10

Teste 3: Entrada: 5 e 5                     Saída: Os valores são iguais.
"""
# Recebe os dois valores digitados pelo usuário
valor1 = float(input("Primeiro valor: "))
valor2 = float(input("Segundo valor: "))

if valor1 > valor2:
    print("O maior valor é", valor1)
elif valor2 > valor1:                           # Senão se ...
    print("O maior valor é", valor2)
else:
    print("Os valores são iguais.")
''' --- ALTERAÇÕES:
a. Se eles forem diferentes, mostre os valores digitados na ordem decrescente
b. Se eles forem iguais, mostre a mensagem e o valor digitado.
                                                                                
'''

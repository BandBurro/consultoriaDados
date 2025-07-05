"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Elabore o programa que gere a sequência dos números naturais
na ordem decrescente de 7 até 0.

- Passos para resolução do problema (algoritmo):
for variavel in range (v_inicial, v_final, v_passo):
    escreva variável do for

- Teste 1:
Saída:
- Ordem decrescente:
7
6
5
4
3
2
1
0
Encerrou a repetição.                   """
print('- Ordem decrescente:')         # Cabeçalho
for decrescente in range(7, -1, -1):  # for decrescente in range(7, 0-1, -1):
    print(decrescente)          # para cada item de 7 e -1, em saltos de -1

print('\nEncerrou a repetição.')
''' ----- ALTERAÇÕES:
a. No final, mostre a quantidade de números da sequência. Use contador. 
   Saída:  Quantidade: 8
b. Mostre também a soma da sequência gerada. Use somador.  
    Teste 2: Saída: Soma = 28
c. Calcule e mostre a média dos números da sequência.

'''

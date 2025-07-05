"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Elabore o programa que gere a sequência dos números naturais
pares até 12.

- Passos para resolução do problema (algoritmo):
for variavel in range (v_inicial, v_final, v_passo):
    escreva variável do for

- Teste:

Saída:

- Números naturais pares:
0
2
4
6
...
12
Encerrou a repetição.

"""
print('- Números naturais pares:')      # Cabeçalho.
for par in range(0, 13, 2):             # for par in range(0, 12+1, 2):
    print(par)                          # Na vertical.
    # Fim da estrutura de repetição for

print('\nEncerrou a repetição.')
''' --- ALTERAÇÕES: 
a. Mostre a sequência dos números na horizontal.
b. Coloque uma vírgula entre os números da sequência.    
c. Substiua a vírgula do último número por um ponto (.). 
d. Obtenha o mesmo resultado, trocando o passo 2 pelo passo 1 no range.

'''

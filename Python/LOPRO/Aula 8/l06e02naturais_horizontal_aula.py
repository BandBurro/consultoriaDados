"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Elabore o programa que gere a sequência dos números naturais até 10 na
horizontal.

- Passos para resolução do problema (algoritmo):
for variavel in range (v_inicial, v_final, v_passo):
    escreva variável do for

- Teste 1 - Saída:

- Números naturais na horizontal:
0 1 2 3 4 5 6 7 8 9 10
Encerrou a repetição.


"""


print("- Números naturais na horizontal:")
for i in range(0, 10+1, 1):  # for i in range(0, 11, 1):  # for i in range(11):
    print(i, end="")  # O end="" evita a quebra de linha, o default é end="\n"
    # Fim da estrutura de repetição for

print('\nEncerrou a repetição.')
''' ----- ALTERAÇÕES:
a. Melhore o layout de saída, colocar um espaço entre os números na horizontal
b. Altere, coloque cinco espaços entre cada número.
c. Retire os cinco espaços e coloque uma vírgula entre os números da sequência.
d. Retire a vírgula do último número da sequência e coloque um ponto final.   
e. Refaça o item anterior sem usar o if ... else.

'''

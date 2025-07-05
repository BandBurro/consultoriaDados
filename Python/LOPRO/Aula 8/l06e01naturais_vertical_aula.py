"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Elabore o programa que gere a sequência dos números naturais até 10 na vertical.

- Passos para resolução do problema (algoritmo):
for variavel in range (v_inicial, v_final, v_passo):
    escreva variável do for

Teste 1 - Saída:

- Números naturais na vertical:
0
1
2
3
...
10
Encerrou a repetição.        """

print('- Números naturais na vertical:')                     # print('Cabeçalho')
for i in range(0, 11, 1):    # for i in range (0, 10+1):     # for i in range(11):
    print(i)                 # Mostra i na tela. O print quebra a linha por padrão
    # Fim da estrutura de repetição for

print('Encerrou a repetição.')

''' ----- ALTERAÇÕES:
a. No final, mostre a quantidade de números da sequência gerada. Use contador. 
   Teste 2: Saída:  Quantidade: 11
b. No final, mostre também a soma dos números da sequência gerada. Use somador.  
   Teste 3: Saída:  Soma = 55
c. Refaça o programa utilizando while em vez de for.

'''

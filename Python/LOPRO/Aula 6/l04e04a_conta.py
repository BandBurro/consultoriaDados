"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:
- Desenvolva o programa que leia vários números digitados pelo usuário
e use o valor -1 como condição (flag) de saída da estrutura de repetição.
Na tela de saída, mostre a quantidade de números digitados.

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para resolução do problema (algoritmo):
variável ct                 # Valor inicial da variável contador
estrutura de repetição:     # início da repetição
    lê número               # Indentação obrigatória
    testa condição saída
    contador                # fim da repetição
tela de saída               # O comando volta para coluna 1
- Sintaxe do while:
. . .       # Os comandos antes do while são executados uma vez, na coluna 1
comandos
. . .
while condição:         # O bloco abaixo será executado várias vezes.
    início do bloco     # Indentação (to indent) obrigatória.
    . . .               # Organizado em colunas
    fim do bloco (repetição while)
. . .       # Os comandos depois do while são executados uma vez, na coluna 1
comandos
. . .
Teste 1: Entrada: 5, 6 e -1          Saída: Quantidade de números: 2
Teste 2: Entrada: 5, 6, 7 e -1       Saída: Quantidade de números: 3
Teste 3: Entrada: 5, 6, 6, 7 e -1    Saída: Quantidade de números: 4
- Problema:
- Desenvolva o programa que leia vários números digitados pelo usuário
e use o valor -1 como condição (flag) de saída da estrutura de repetição.
Na tela de saída, mostre a quantidade de números digitados      """
ct = 0              # Valor inicial da variável
print('Digite [-1] para sair da repetição')
while True:  # Laço de repetição, repete enquanto condição verdadeira
    numero = int(input("Digite um número: "))  # Indentação obritória
    if numero == -1:
        break       # Sai de uma estrutura de repetição (while)
    ct = ct + 1     # ct += 1 (contador), incrementa o ct
    # Fim da estrutura de repetição "while"
print('Quantidade de números digitados:', ct)  # O comando volta para coluna 1
''' --- ALTERAÇÕES:
a. Na tela de saída, acrescente a soma dos valores digitados.
    --- DICAS:                                        '''
ct = 0              # Valor inicial das variáveis               # a.
soma = 0
print('Digite [-1] para sair')
while True:  # Laço de repetição, repete enquanto condição verdadeira
    numero = int(input("Digite um número: "))  # Indentação obritória
    if numero == -1:
        break       # Sai de uma estrutura de repetição (while)
    ct = ct + 1     # ct += 1 (contador), incrementa o ct
    soma = soma + numero  # soma += numero (somador ou acumulador)
    # Fim da estrutura de repetição "while"
print('Quantidade de números digitados:', ct)  # O comando volta para coluna 1
print("Soma dos valores digitados:", soma)



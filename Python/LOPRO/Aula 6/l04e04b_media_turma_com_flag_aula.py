"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

vbc-shqr-wxd (Meet)

- Problema:

- Desenvolva o programa que calcule a média aritmética de uma turma,
onde cada aluno realizou uma avaliação. Não sabemos a quantidade de
alunos, por isso usaremos o valor “-1” como condição (flag) de saída.
Na tela de saída, mostre a média aritmética da turma e a quantidade
de alunos da turma.

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para resolução do problema (algoritmo):
variável ct                 # Valor inicial das variáveis
variável soma
estrutura de repetição:     # Início da repetição
    lê número
    testa condição saída
    contador
    somador                 # Fim da repetição
calcula média               # Os comandos voltam para coluna 1
tela de saída

- Dica: media = soma / ct

         - Entrada:     - Saída:
Teste 1: 5, 6 e -1      Média 5.5               Quantidade: 2
Teste 2: 5, 6, 7 e -1   Média 6                 Quantidade: 3
Teste 3: 5, 6, 6 e -1   Média 5.666666666666667 Quantidade: 3   """

ct = 0                  # Valor inicial das variáveis
soma = 0
print('Digite [-1] para sair')
while True:  # Laço de repetição while, repete enquanto condição verdadeira
    nota = float(input("Nota do aluno: "))  # Indentação é obritória
    if nota == -1:
        break           # Sai de uma estrutura de repetição (while)
    ct = ct + 1         # ct += 1 (contador), incrementa o ct
    soma = soma + nota  # soma += nota (somador ou acumulador)
    # Fim da estrutura de repetição "while"
media = soma / ct       # Os comandos voltam para coluna 1
print("Média da turma:", media)
print('Quantidade de alunos:', ct)

''' --- ALTERAÇÕES:
a. Mostre também a soma das notas dos alunos da turma.
b. Mostre a média da turma com duas casas decimais.
c. No início do programa, leia o nome do professor da turma. 
d. E no final, na tela de saida, mostre também o nome do professor da turma
e. Mostre a média e a quantidade de alunos na mesma linha, nesta frase:
   A média da turma de X alunos é X.XX.
f. Se digitar -1 na primeira leitura ocorre o erro: 
   "ZeroDivisionError: division by zero". 
   Resolva esse problema e faça o teste 4 
   Teste 4: Entrada: notas: -1         Saída: Não existe divisão por zero.
g. Troque a mensagem estática da entrada de dados (input) por uma mensagem 
   dinâmica.

'''

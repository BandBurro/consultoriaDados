"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

vbc-shqr-wxd (Meet)

- Problema:

- Construa o programa que calcule a média aritmética dos números pares.
O usuário fornecerá os valores de entrada que pode ser um número
qualquer par ou ímpar. A condição de saída será o número 0 (zero).

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para resolução do problema (algoritmo):
variável ct                 # Valor inicial das variáveis
variável soma
estrutura de repetição:     # Início da repetição
    lê número
    testa condição saída
    se número é par?
        contador
        somador             # Fim da repetição
calcula média               # Os comandos voltam para coluna 1
tela de saída

- Dicas:
1. media = soma / ct
2. O operador modulo (%) pega o resto da divisão de dois números.

Teste 1: Entrada: valor: 1, 2 e 0           Saída: Média 2
Teste 2: Entrada: valor: 1, 2, 3, 4 e 0     Saída: Média 3
Teste 3: Entrada: valor: 1, 2, 2, 4 e 0     Saída: Media 2.6666666666666665     """

ct = 0                  # Contador, conta os números pares
soma = 0                # Somador, soma os números pares
# ct = soma = 0         # Inicializa todas as variáveis numa linha
print('Digite zero [0] para sair')
while True:             # while valor != 0:
    valor = int(input("Digite um número: "))  # Recebe um número inteiro
    if valor == 0:      # valor igual (==) a 0 é a condição de saída
        break           # O break força a saída da estrutura de repetição
    resto = valor % 2   # O operador % pega o resto da divisão
    if resto == 0:      # Se o resto for zero o valor é par
        soma = soma + valor     # soma += valor
        ct = ct + 1             # ct += 1  # incrementa a contagem
    # Fim da estrutura de repetição "while"
media = soma / ct               # Os comandos voltam para coluna 1
print("A média de todos os pares é:", media)  # Mostra o resultado

''' --- ALTERAÇÕES:
a. Mostre a média com quatro casas decimais.
b. Mostre a quantidade de números pares.
c. Mostre a quantidade de números digitados.
d. Como resolver o teste 4, corrija esta mensagem de erro do Python.
   Teste 4: valor: 1, 3 e 0        Saída: Não foi digitado número par. 

'''

"""               Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha

- Operadores aritméticos:
    +   →   soma
    –   →   subtração
    *   →   multiplicação
    /   →   divisão
    //  →   divisão de inteiros (quociente da divisão)
    %   →   módulo (resto da divisão)
    **  →   potenciação

1- Como criar um projeto no IDE PyCharm:
   - File - New Project - Create
2- Como criar um programa dentro do projeto:
   - Coluna esquerda - mouse direito no nome do projeto (PythonProject)
   New - Python File
   - Digite o nome do programa Python sem espaço e sem acentuação - <Enter>
3- Como roda (executa) o programa:
   - Run - Run, ou use as teclas de atalho.

- Exercício (problema):
- Elabore o programa que calcule a soma de dois valores inteiros que serão
fornecidos pelo usuário.

- Ideia (lógica) para resolver o problema: preciso de quantas variáveis?

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: valores 1 e 2.            Saída: 3

Fim do Comentário de várias linhas.     """

# Recebe os valores convertidos para número inteiro
valor1 = int(input("Digite o primeiro valor: "))        # Entrada de dados
valor2 = int(input("Digite o segundo valor: "))

soma = valor1 + valor2  # Calcula e atribui o resultado à variável soma (processamento)

print("A soma é igual a", soma)                         # Saída

''' ----- ALTERAÇÕES:
a. No final do programa, acrescente a subtração dos valores lidos e
   mostre o resultado.
b. No final do programa, acrescente a multiplicação dos valores lidos e
   mostre o resultado. 
c. No final do programa, leia mais um valor inteiro, ou seja, o terceiro
   valor inteiro.
d. No final do programa, acrescente a soma dos três valores lidos e mostre
   o resultado.

'''

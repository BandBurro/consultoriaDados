"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Operadores aritméticos:
    +   →   soma
    –   →   subtração
    *   →   multiplicação
    /   →   divisão
    //  →   divisão de inteiros (quociente da divisão)
    %   →   módulo (resto da divisão)
    **  →   potenciação

Crie um novo programa dentro do mesmo projeto:
- Coluna esquerda - mouse direito no nome do projeto (PythonProject)
  New - Python File
- Digite o nome do programa Python sem espaço e sem acentuação - <Enter>

- Problema:
- Projete o programa para calcular a área de um triângulo. O usuário 
informará os dados necessários para o cálculo, ou seja, a base e a 
altura do triângulo.

- Fórmula:     área = base . altura
                            2

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: base: 1.5 e altura: 2.6   Saída: 1.9500000000000002

Fim do Comentário de várias linhas.     """

# Calcular a área de um triângulo.
base = float(input("Digite a base: "))  # Recebe um valor real do usuário
altura = float(input("Digite a altura: "))

area = base * altura / 2                # Processamento

print("Área:", area)                    # Saída

''' --- ALTERAÇÕES:
a. Na tela de saída de dados, mostre também o valor da base e da altura.
b. Mostre o valor da área com três casas decimais.

'''

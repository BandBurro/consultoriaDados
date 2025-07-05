"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

vbc-shqr-wxd (Meet)

- Problema anterior:
- Analise o resultado de uma transação comercial. Verifique a situação final
do comerciante trabalhando com os valores lidos, ou seja, o preço de compra
e o preço de venda. Gere a tela de saída com uma das seguintes mensagens:
“Teve lucro.”, “Teve prejuízo.” ou “Os valores são iguais.”.

- Problema atual:
- Refaça o programa anterior. Se os valores forem diferentes, mostre também
o valor do lucro em reais ou o valor do prejuízo em reais.

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
processamento (cálculo)
Testes (se ...)
Saída de dados (escreva)

Teste 1: Entrada: compra = 1000 e venda = 1200  Saída: Lucro = 200
Teste 2: Entrada: compra = 1200 e venda = 1000  Saída: Prejuízo = 200
Teste 3: Entrada: compra = 1000 e venda = 1000  Saída: Os valoes são iguais.
"""
# Recebe os valores de compra e venda
# Lê o valor, converte para float e atribui à variável
vl_compra = float(input("Preço de compra: "))
vl_venda = float(input("Preço de venda: "))

transacao = vl_venda - vl_compra      # calcula o lucro da venda

if transacao > 0:    # Se venda > compra, houve lucro
    print("A transação teve lucro de R$", transacao)
elif transacao < 0:  # Se venda < compra, ou seja, houve prejuízo
    print(f"A transação teve prejuízo de R${-transacao}")  # Multiplica por -1
else:                # Se venda = compra, não houve lucro ou prejuízo
    print("A transação não resultou em lucro nem prejuízo.")

"""
--- Alterações:
a. Mostre o valor do lucro ou do prejuízo com duas casas decimais
b. Na tela de saída, mostre também o valor do preço de compra e 
   do preço de venda.
c. Peça para o usuário digitar também o nome do produto.
d. Mostre o nome do produto na tela de saída.

"""

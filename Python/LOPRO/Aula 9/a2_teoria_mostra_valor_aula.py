"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Crie uma função (def) que recebe um valor e mostra o valor recebido.
  A função main (principal) chama a função três vezes, passa um valor
inteiro positivo, um valor float e depois um valor inteiro negativo. """

# O def indica o início de uma função (uma rotina)
def mostra_valor(p_valor):  # Assinatura da função
    print("Parâmetro recebido:", p_valor)

# Chama a função (def) dentro do main.
# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':  # Função principal, atalho: mai + <tab>
   # Primeira forma de fazer (sem variáveis, passa o valor direto):
    mostra_valor(5)         # Chama a função
    mostra_valor(23.8)      # Chama a função
    mostra_valor(-55)       # Chama a função

''' ----- ALTERAÇÕES:
a. No main, chame a função mais três vezes, agora, passe os três 
   valores usando atribuição e variável.
b. No main, chame a função mais três vezes, agora, passe os três 
   valores que serão digitados pelo usuário. 
c. Crie mais uma função para mostrar dois valores, ela recebe dois 
   valores e mostra os dois valores. 
d. No main, chame a função mostra_dois_valores passando os números 5 e 10.
e. Chame a função mostra_dois_valores novamente, o usuário digita os 
   dois valores na função principal (main)
    ----- DICAS:
    # Segunda forma de fazer (com variáveis, sem input):        # a.
    v_inteiro = 5
    mostra_valor(v_inteiro)   # Chama a função
    numero = 23.8
    mostra_valor(numero)    # Chama a função
    negativo = -55
    mostra_valor(negativo)  # Chama a função
    # Terceira forma de fazer (com variáveis, com input):       # b.
    v_inteiro = int(input("valor"))
    mostra_valor(v_inteiro)  # Chama a função
    v_real = float(input("valor"))
    mostra_valor(v_real)      # Chama a função
    v_negativo = int(input("valor"))
    mostra_valor(v_negativo)  # Chama a função
def mostra_dois_valores(valor1, valor2):                        # c.

    print("Valor 1: ", valor1)
    print("Valor 2: ", valor2)
if __name__ == '__main__':                                      # d.
    ...
    mostra_dois_valores(5, 10)
    v1 = input("Valor 1: ")                                     # e.
    v2 = input("Valor 2: ")
    mostra_dois_valores(v1, v2)        

'''

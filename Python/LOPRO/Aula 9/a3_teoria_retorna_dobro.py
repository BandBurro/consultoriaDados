"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Implemente a função calcula o dobro. Ela recebe um valor, calcula o
dobro e retorna o valor calculado. Não use o print dentro desta função.

- A função principal (main) lê um valor digitado pelo usuário, chama
a função passando o argumento (o valor lido) e mostra o valor retornado
pela função calcula o dobro.

- Teste:
Entrada: 5         Saída: Valor retornado pela função: 10
"""
# O def indica o início de uma função (uma rotina)
def calcula_dobro(p_valor):               # Assinatura da função
    dobro = p_valor * 2
    return dobro
# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':  # Função principal, atalho: mai + <tab>
    valor = int(input("Valor inteiro: "))
    v_retornado = calcula_dobro(valor)  # Chama a função
    # A variável valor_retornado recebe o valor retornado pela função (def)
    # O valor retornado pela função é armazenado na variável v_retornado
    print("Valor retornado pela função:", v_retornado)
''' --- ALTERAÇÕES:
a. Acrescente a função calcula triplo. Ela recebe um valor, calcula
   o triplo e retorna o valor calculado.
b. No final do main (função principal) chame a função e mostre o valor 
   retornado pela função calcula triplo.
c. Refaça a função main sem usar a variável valor_retorno.
    --- Dicas:
def calcula_triplo(p_valor):                                    # a.
    triplo = p_valor * 3
    return triplo
if __name__ == '__main__':                                      # b.
    ...
    v_retornado2 = calcula_triplo(valor)  # No final da função principal
    print(v_retornado2)
    ...
    # v_retornado = calcula_dobro(valor)                      # c.
    # print("Valor retornado pela função:", v_retornado)
    print("Valor retornado pela função:", calcula_dobro(valor))

'''

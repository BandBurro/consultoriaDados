"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Crie uma função para somar dois valores. Ela recebe os dois parâmetros
(valores), calcula a soma e retorna o resultado do cálculo.

- A função main lê os dois valores inteiros digitados pelo usuário,
chama a função passando os valores lidos e depois mostra o valor
retornado pela função, ou seja, o resultado obtido.
Teste: Entrada: 3 e 2                   Saída: Soma = 5         """

# O def define a função que recebe os parâmetros (valores) v1 e v2.
def retorna_soma(v1, v2):          # Assinatura da função
    soma = v1 + v2                 # A variável soma recebe o cálculo
    return soma                    # Retorna o valor calculado
    # Fim da funçao
# A função (def) só será executada quando for chamada na função main.
# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':                   # mai + <tab> (atalho)
    valor1 = int(input('Primeiro valor: '))  # Indentação obrigatória.
    valor2 = int(input('Segundo valor: '))
    v_retorno = retorna_soma(valor1, valor2)  # Chama a função
    # A variável v_retorno recebe o valor retornado pela função (def)
    print("Soma = ", v_retorno)
    v_retorno = retorna_soma(2.1, 3.3)  # No final do main      # a.
    print ("Soma = ", v_retorno)
''' --- ALTERAÇÕES:
a. Acrescente, chame a função retorna_soma mais uma vez, passe os 
   valores reais (2.1, 3.3). 
b. Acrescente (crie) a função retorna_soma_2, refaça a função sem usar  
   a variável soma.
c. Acrescente (crie) a função mostra_soma. Ela recebe dois valores, faz 
   a soma, mostra o resultado do cálculo e não retorna nada. 
d. Na função main, teste a função mostra_soma, ou seja, chame a função 
   mostra_soma passando os valores lidos.        
    --- DICAS ABAIXO:
    v_retorno = retorna_soma(2.1, 3.3)  # No final do main      # a.
    print ("Soma = ", v_retorno)
def retorna_soma_2(v1, v2):                                     # b.
    # soma = v1 + v2               
    # return soma                  
    return v1 + v2                                           
e. Acrescente mais uma função. A função somaTres recebe três valores 
   inteiros e retorna a soma dos três valores.
    --- DICAS ABAIXO:
    v_retorno = retorna_soma(2.1, 3.3)  # No final do main      # a.
    print ("Soma = ", v_retorno)

def retorna_soma_2(v1, v2):                                     # b.
    # soma = v1 + v2               
    # return soma                  
    return v1 + v2                                           
    ...                          # Acrescente no final do main
    v_retorno = retorna_soma_2(valor1, valor2)  
    print("Soma = ", v_retorno)
def mostra_soma(v1, v2):                                        # c.
    valor = v1 + v2                  
    print ("Soma = ", valor)
    # Fim da funçao mostra_soma.   
if __name__ == '__main__':                                      # d.
    . . .    
    mostra_soma(valor1, valor2)  # Chama a função que não retorna nada.

'''

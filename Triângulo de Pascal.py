# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 02:54:23 2020

@author: d-nct
"""
# Início do triângulo de Pascal
#1
#1 1
#1 2 1
#1 3 3  1
#1 4 6  4  1
#1 5 10 10 5  1
#1 6 15 20 15 6  1
#1 7 21 35 35 21 7  1

# Caso base:
# L_{0} = [1]

# Recorrência:
# L_{n}[i] = L_{n-1}[i-1] + L_{n-1}[i]
# if primeira_coluna (L_{n-1}[i-1]):
#    L_{n-1}[i-1] = 1
# if ultima_coluna (L_{n-1}[i])
#    L_{n-1}[i]

def pascal_elemento (i, j):
    """Retorna o elemento do Triângulo de Pascal (combinação) de "coordenadas" (i,j), lembrando que a contagem começa em 0!"""
    assert (i >= 0 or j >= 0 or j <= i), "Esse elemento não existe!"

    # estabelecemos os caso base
    if i == j or j == 0:
        return 1

    # e a recorrência
    else:
        return pascal_elemento(i-1,j) + pascal_elemento (i-1,j-1)


cache_elemento = {}
def pascal_elemento_memoizada (i, j):
    """Retorna o elemento do Triângulo de Pascal (combinação) de "coordenadas" (i,j), lembrando que a contagem começa em 0!"""
    assert (i >= 0 or j >= 0 or j <= i), "Esse elemento não existe!"
    
    if (i,j) in cache_elemento:
        return cache_elemento[(i,j)]
    
    # estabelecemos os caso base
    if i == j or j == 0:
        return 1

    # e a recorrência
    else:
        result = pascal_elemento_memoizada(i-1,j) + pascal_elemento_memoizada (i-1,j-1)
        cache_elemento[(i,j)] = result
        return result


def pascal (L):
    """Imprime o Triângulo de Pascal com L linhas"""
    assert (L >= 0), "O número de linhas deve ser maior ou igual a zero!"

    L += 1 # para a contagem das linhas partir de 0
    A = [[x] for x in range (L)] #construímos as linhas, sem prestar atenção nos valores

    # e as colunas -1
    return [[pascal_elemento_memoizada(i,j) for j in range(A[i][0]+1)] for i in range (L)]

def tamanho_do_maior_elemento(triângulo):
    """Retorna o tamanho do maior algarismo do triângulo.
    """
    tamanho = 0
    for elemento in triângulo[len(triângulo)-1]: # O maior elemento está na última linha.
        if len(str(elemento)) > tamanho:
            tamanho = len(str(elemento))
    return tamanho

def imprime_triângulo(triângulo):
    """Imprime o Triângulo de Pascal de entrada.
    """
    maior_tamanho = tamanho_do_maior_elemento(triângulo)
    # Imprimimos o primeiro e o último 1 separados para podermos imprimir os separadores
    for linha in triângulo:
        print (f'{linha[0]:^{maior_tamanho}} ', end='')
        for elemento in linha[1:-1]:
            print (f'| {elemento:^{maior_tamanho}} ', end='')
        if linha != [1]:
            print (f'| {linha[len(linha)-1]:^{maior_tamanho}}', end='')
        print() # Quebramos a linha ao final de cada linha impressa.

def chamar_triângulo ():
    """Para a execução do código.
    """
    try:
        altura = int(input("\nInsira a altura do Triângulo de Pascal, lembrando que a contagem começa do zero: \n"))
    except ValueError:
        print ("Algo saiu errado... \nA altura do Triângulo deve ser um número inteiro!")
        return
    print("\nEntendido, é pra já:\n")
    
    imprime_triângulo(pascal(altura))
    
    print ("\nFeito! Deseja imprimir mais um?")
    repetição = input("Digite <t> para imprimir outro triângulo; <e> para imprimir um elemento; e <enter> para sair: \n")
    if repetição == 't':
        chamar_triângulo()
    elif repetição == 'e':
        chamar_item()

def chamar_item():
    """Imprime um ítem específico do triângulo de coordenadas (a,b):
    """
    print("\nVamos imprimir o elemento do triângulo de coordenada (a,b). Para tal, diga qual é esse elemento.")
    try:
        a = int(input("Digite o 'a': \n"))
        b = int(input("Digite o 'b': \n"))
    except ValueError:
        print("\nAlgo saiu errado... \nAs coordenadas do elemento devem ser números inteiros!")
        chamar_item()

    item = pascal_elemento_memoizada (a,b)
    print(f"\nTá na mão pae: ({a},{b}) no triângulo é {item}")
    repetição = input("\nPara calcular outro elemento específico, digite <e>; para imprimir o Triângulo, digite <t>; e <enter> para sair: \n")
    if repetição == 'e':
        chamar_item()
    elif repetição == 't':
        chamar_triângulo()

print(
"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                        Seja bem vind@!
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""")

opção = input(
"""Digite <enter> para seguir com o Triângulo; ou
Digite <e> para calcular um elemento específico de coordenada (a,b), isto é, a combinação de a escolhendo b elementos: \n> """
            )

if opção == '':
    chamar_triângulo()
elif opção == 'e':
    chamar_item()
def achar_vencedor(lista):
    '''A função pega uma lista de números e printa o número i 
    se ele for igual a sua posição na fila, como a posição na
    lista começa em 0, o elemento da posição i, deve ser igual 
    a i + 1'''
    for i in range(len(lista)):
        if lista[i] == i + 1:
            print(lista[i])

j = 1
while True:
    
    N = int(input())

    if N == 0:
        break

    participantes = [int(x) for x in input().split()]
    #pesquisei como faz um input com tamanhos variáveis
    
    print(f"Teste {j}")
    achar_vencedor(participantes)
    j += 1

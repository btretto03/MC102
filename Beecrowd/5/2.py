def faz_lista(num2):
    '''A função recebe um numero e devolve uma lista com seus algarismos
    '''
    lista2 = []
    for x in num2:
        lista2.append(x)
    return lista2

def retira(num1, lista2):
    '''A funcao recebe um numero e uma lista de numeros e devolve uma nova lista
    com todos elementos menos os que forem iguais a num1
    '''
    lista3 = []
    for x in lista2:
        if x != num1:
            lista3.append(x)
    return lista3

def corrige_zeros(lista):
    '''A função garante que se aparecer algum número como 0000 na lista, apareça somente 0 e apaga os zeros a esquerda'''
    while lista and lista[0] == '0':
        lista.pop(0)
    if  len(lista) == 0:
        return ['0']
    
    return lista


while True:
    num1, num2 = input().split()
    if num1 == "0" and num2 == "0":
        break
    
    lista2 = faz_lista(num2)
    listaremov = retira(num1, lista2)
    listavalida = corrige_zeros(listaremov)
    print(*listavalida, sep = '')
def faz_lista(frase):
    '''A função recebe uma string e devolve uma lista com as suas letras
    '''
    lista_letras = []
    for letra in frase:
        lista_letras.append(letra)
    return lista_letras

def combina(lista1,lista2):
    '''A funcao recebe duas listas e as combina conforme pedido no enunciado
    '''
    listacombinada = []
    for x in lista1:
        listacombinada.append(x)
    i = 0
    for y in lista2:
        listacombinada.insert(1+i, y)
        i += 2

    return listacombinada


vezes = int(input())
for _ in range (vezes):
    txt1, txt2 = input().split()
    lista1 = faz_lista(txt1)
    lista2 = faz_lista(txt2)
    print(*combina(lista1, lista2), sep = '')
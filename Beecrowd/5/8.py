def faz_lista(frase):
    '''A função recebe uma string e devolve uma lista com as suas letras
    '''
    lista_letras = []
    for letra in frase:
        lista_letras.append(letra)
    return lista_letras


def italico(lista):
    '''A funcao recebe uma lista e transforma seus elementos _'''
    under = True #garante que o primeiro _ será trocado por um <i> sem a barra
    for i in range(len(lista)):
        if lista[i] == '_':
            if under:
                lista[i] = '<i>'
            else:
                lista[i] = '</i>'
            under = not under
    return lista
        
def negrito(lista):
    '''A funcao recebe uma lista e transforma seus elementos *'''
    under = True   #garante que o primeiro * será trocado por um <b> sem a barra
    for i in range(len(lista)):
        if lista[i] == '*':
            if under:
                lista[i] = '<b>'
            else:
                lista[i] = '</b>'
            under = not under
    return lista

while True:
    try:
        frase = negrito(italico(faz_lista(input())))
        print(*frase, sep = '')
        
    except EOFError:
        break
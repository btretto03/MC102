def desloca_1(frase):
    '''A funcao recebe uma frase e move suas letras 3 posicoes para a direita na tabela ASCII
    '''
    resultado = ''
    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >=97 and ord(letra)<=122:
            resultado += chr(ord(letra) + 3)
        else:
            resultado += letra
    return resultado

def inverte(frase):
    '''A funcao inverte os caracteres de uma frase'''
    resultado =''
    for letra in frase[::-1]:
        resultado += letra
    return resultado

def desloca_2(frase):
    '''Qualquer caractere a partir da metade (truncada) em diante deve ser deslocado uma posição para a esquerda na tabela ASCII.'''
    y = len(frase) // 2
    nova_frase = frase[:y]
    for c in frase[y:]:
        nova_frase += chr(ord(c) - 1)
    return nova_frase


vezes = int(input())
for _ in range(vezes):
    frase = desloca_2(inverte(desloca_1(input())))
    print(frase)


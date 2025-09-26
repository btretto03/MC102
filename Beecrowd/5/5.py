def dancante(frase):
    '''A função pega uma frase aleatória e a transforma em dançante.'''
    resultado = ""
    maiuscula = True   # para começar com maiúscula
    for x in frase:
        if x != ' ':
            if maiuscula:
                resultado += x.upper()
            else:
                resultado += x.lower()
            maiuscula = not maiuscula #retorna pra minuscula
        else:
            resultado += ' '
    return resultado

while True:
    try:
        frase = input()
        print(dancante(frase))
    except EOFError:
        break
    #estava dando EOFError no beecrowd, entao tentei trabalhar com excecao
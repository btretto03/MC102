def linha(frase, carac):
    '''A funcao recebe uma frase e a quantidade maxima de caracteres por linha e cria uma nova lista com as listas das linhas do texto
    '''
    palavras = frase.split()  # Cria uma lista com as palavras da frase
    texto = []
    linhax = []
    comprimento = 0

    for palavra in palavras:
        if comprimento == 0:
            linhax.append(palavra)
            comprimento = len(palavra)
        elif comprimento + len(palavra) + 1 <= carac:  # Cabe na linha com espaço
            linhax.append(palavra)
            comprimento += 1 + len(palavra)  # Soma 1 por causa do espaço
        else:
            texto.append(linhax)  # Adiciona a linha e começa uma nova
            linhax = [palavra]
            comprimento = len(palavra)

    
    if linhax != []:  #se ainda soubrar palavras
        texto.append(linhax)

    return texto


while True:
    try:
        pal, lin, carac = map(int, input().split()) 
        frase = input()
        
        texto = linha(frase, carac)
        linhas = len(texto)
        paginas = (linhas + lin - 1) // lin 

        print(paginas)

    except EOFError:
        break
def resposta(a, b, c, d, e):
    '''A função analisa as respostas e compara com as alternativas, printa a sua correspondente, se o tamanho
    da lista respostas for diferente de um significa que o estudante assinalou mais de uma resposta e assim terá sua questao
    anulada'''
    lista = [a, b, c, d, e]
    resposta = []
    s = min(lista)
    indice = lista.index(s)
    for i in (lista):
        if i <= 127:
            resposta.append(i)
    s = len(resposta)
    if s != 1:
        print('*')
    elif indice == 0:
        print('A')
    elif indice == 1:
        print('B')
    elif indice == 2:
        print('C')
    elif indice == 3:
        print('D')
    elif indice == 4:
        print('E')
    
while True:
    N = int(input())
    if N == 0:
        break
    
    i = 0
    while i < N:
        a, b, c, d, e = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)

        resposta(a, b, c, d, e)

        i += 1
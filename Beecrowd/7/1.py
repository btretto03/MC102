def criar_lista(lista):
    '''A funcao recebe uma lista e cria varias listas uma para cada elemento da lista original com ele ja inserido, retornando
    uma outra lista com as listas de numeros'''
    listanumeros= []
    for x in lista:
        listanova = []
        listanova.append(x)
        listanumeros.append(listanova)
    return listanumeros

def adiciona(lista):
    '''Adiciona cada caractere na sublista correspondente'''
    global numeroslinha1
    for i in range(len(lista)):
        numeroslinha1[i].append(lista[i])
    return numeroslinha1

def cria_numeros():
    '''Transforma cada coluna (lista de 4 dígitos) em um número inteiro'''
    listanumeros = []
    for i in range(len(numeroslinha1)):
        numero = ""
        for j in range(len(numeroslinha1[i])):
            numero += numeroslinha1[i][j]
        listanumeros.append(int(numero))
    return listanumeros



linha1 = input().strip()
linha2 = input().strip()
linha3 = input().strip()
linha4 = input().strip()

numeroslinha1 = criar_lista(linha1)
adiciona(linha2)
adiciona(linha3)
adiciona(linha4)

listanumeros = cria_numeros()
numF = int(listanumeros[0])
numL = int(listanumeros[-1])

texto = ""
for j in range(1, len(listanumeros) -1):
    carac  = chr((numF * int(listanumeros[j]) + numL) % 257)
    texto += carac

print(texto)

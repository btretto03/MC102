def inteiros(a, b, c):
    ''' a função recebe três valores e os retorna como inteiros'''
    a = int(a)
    b = int(b)
    c = int(c)
    return a, b, c

def adicionar_na_lista(a, b, c, d, e, f):
    ''' a função recebe seis variáveis e as adiciona na lista'''
    global lista
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)
    lista.append(e)
    lista.append(f)
    return lista

def soma_lista(lista, inicio, passo):
    '''Soma elementos de uma lista começando do índice `inicio`
    e pulando de `passo` em `passo`.'''

    
    return sum(lista[i] for i in range(inicio, len(lista), passo))


nmrjogadores = int(input())

i = 0
while i < nmrjogadores:
    nome = input()
    lista = []
    saq, bloq, ata = input().split()
    saq, bloq, ata = inteiros(saq, bloq, ata)
    saqef, bloqef, ataef = input().split() #ef = efetivo
    saqef, bloqef, ataef = inteiros(saqef, bloqef, ataef)

    adicionar_na_lista(saq, saqef, bloq, bloqef, ata, ataef) # Como cada elemento na lista tem posição constante, posso somar com o mesmo passo
                                                             # se eu pegar um elemento saque depois de  elementos será outro saque
    i += 1


porcenataques = round(soma_lista(lista, 5, 6)/soma_lista(lista, 4, 6)*100,2) # no Beecrowd estava dando errado por arredondamento
porcensaques = round(soma_lista(lista, 1, 6)/soma_lista(lista, 0, 6)*100,2)
porcenbloq = round(soma_lista(lista, 3, 6)/soma_lista(lista, 2, 6)*100,2)

print(f"Pontos de Saque: {porcensaques:.2f} %")
print(f"Pontos de Bloqueio: {porcenbloq:.2f} %")
print(f"Pontos de Ataque: {porcenataques:.2f} %")


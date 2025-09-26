def inteiros(a, b, c):
    ''' a função recebe três valores e os retorna como inteiros'''

    a = int(a)
    b = int(b)
    c = int(c)

    return a, b, c

def calculo_HP(bs, iv, ev, nivel):
    '''A função recebe 4 variáveis e calcula o valor de hp final'''
    
    hp = (iv + bs + (ev)**0.5/8 + 50)*nivel//50 + 10
    
    return hp

def calculo_outras(bs, iv, ev, nivel):
    '''A função recebe 4 variáveis e calcula o valor final das outras atribuições'''

    atribut = (iv + bs + (ev)**0.5/8)*nivel//50 + 5

    return atribut


vezes = int(input())

for i in range(1, vezes+1):
    nome,nivel = input().split()
    nivel = int(nivel)
    print(f"Caso #{i}: {nome} nivel {nivel}")

    bs, iv, ev = input().split()
    bs, iv, ev = inteiros(bs, iv, ev)
    
    hp = calculo_HP(bs, iv, ev, nivel)
    print(f"HP: {hp:.0f}")

    lista = ["AT", "DF", "SP"]

    for j in lista:
        bs, iv, ev = input().split()
        bs, iv, ev = inteiros(bs, iv, ev)
        atribut = calculo_outras(bs, iv, ev, nivel)
        print(f"{j}: {atribut:.0f}")

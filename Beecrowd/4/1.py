def somarafael(x, y):
    '''Faz a soma do Rafael com os parâmetros x e y'''
    r = 9*(x**2) + y**2
    return r

def somabeto(x, y):
    '''Faz a soma do Beto com os parâmetros x e y'''
    b = 2 *(x**2) + 25*(y**2)
    return b

def somacarlos(x,y):
    '''Faz a soma do Carlos com os parâmetros x e y'''
    c = (-100)*x + y**3
    return c


qntvezes = int(input())

i = 0
while i < qntvezes:
    x, y = input().split()
    x = int(x)
    y = int(y)

    r = somarafael(x, y)
    b = somabeto(x, y)
    c = somacarlos(x, y)

    if r > b and r > c:
        print("Rafael ganhou")
    if b > r and b > c:
        print("Beto ganhou")
    if c > r and c > b:
        print("Carlos ganhou")

    i += 1


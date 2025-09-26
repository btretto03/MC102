def quadrante(a, b):
    '''A função recebe valores de a e b e analisa comparando 
     com a origem para devolver em qual quadrante(direção) eles estão'''
    global origem1
    global origem2
    if a > origem1 and b > origem2:
        print("NE")
    elif a > origem1 and b < origem2:
        print("SE")
    elif a < origem1 and b > origem2:
        print("NO")
    elif a < origem1 and b < origem2:
        print("SO")
    elif a == origem1 or b == origem2:
        print("divisa")

while True:
    vezes = int(input())

    if vezes == 0:
        break

    origem1, origem2 = input().split()
    origem1 = int(origem1)
    origem2 = int(origem2)

    i = 0
    while i < vezes:
        a, b = input().split()
        a = int(a)
        b = int(b)

        quadrante(a,b)

        i += 1

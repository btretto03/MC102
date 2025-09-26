def potencia(base, expoente):
    ''' funcao recursiva que calcula potencia e tem como base o expoente 1'''
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)

vezes = int(input())

i = 1
while i <= vezes:
    print(i, potencia(i, 2), potencia(i, 3))
    i += 1
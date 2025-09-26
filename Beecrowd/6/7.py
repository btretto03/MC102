def comparar(a, b):
    '''A funcao compara os elementos dizendo qual e maior'''
    if a[1][0] > b[1][0]:
        return True
    elif a[1][0] < b[1][0]:
        return False
    if a[1][1] > b[1][1]:
        return True
    elif a[1][1] < b[1][1]:
        return False
    if a[1][2] > b[1][2]:
        return True
    elif a[1][2] < b[1][2]:
        return False
    return a[0] < b[0]

def insertion_sort(lista):
    ''' A funcao ordena as listas'''
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and not comparar(lista[j], atual):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual

paises = {}
try:
    while True:
        modalidade = input()
        ouro = input()
        prata = input()
        bronze = input()

        if ouro not in paises:
            paises[ouro] = [0, 0, 0]
        paises[ouro][0] += 1

        if prata not in paises:
            paises[prata] = [0, 0, 0]
        paises[prata][1] += 1

        if bronze not in paises:
            paises[bronze] = [0, 0, 0]
        paises[bronze][2] += 1

except EOFError:
    pass

print("Quadro de Medalhas")
lista = list(paises.items())
insertion_sort(lista)

for pais, medalhas in lista:
    print(f"{pais} {medalhas[0]} {medalhas[1]} {medalhas[2]}")
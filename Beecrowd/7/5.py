while True:
    num = int(input())
    if num == 0:
        break

    matriz = []    
    for i in range(num):
        linha = []
        for j in range(num):
            valor = 1 + min(i, j, num - 1 - i, num - 1 - j)
            linha.append(valor)
        matriz.append(linha)
    
    for linha in matriz:
        print(" ".join(f"{x:3d}" for x in linha))
    print()
    
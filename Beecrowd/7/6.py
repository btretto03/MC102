while True:
    num = int(input())
    if num == 0:
        break

    matriz = []
    for i in range(num):
        linha = []
        for j in range(num):
            valor = abs(i - j) + 1
            linha.append(valor)
        matriz.append(linha)
    
    for linha in matriz:
        for k in range(len(linha)):
            s = str(linha[k])
            # calcula quantos espaços colocar para completar 3 caracteres
            espacos = 3 - len(s)
            if k == len(linha) - 1:
                # último elemento da linha, sem espaço no final
                print(" " * espacos + s)
            else:
                # elementos intermediários, com um espaço após
                print(" " * espacos + s, end=' ')
    print()
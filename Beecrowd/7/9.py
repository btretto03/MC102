while True:
    try:
        vezes = int(input())

        matriz = []

        for i in range(vezes):
            linha = []
            for j in range(vezes):
                linha.append(0)  # Inicializa tudo com 0
            matriz.append(linha)

        # Preenche a diagonal principal com 2
        for i in range(vezes):
            matriz[i][i] = 2

        # Preenche a diagonal secundária com 3
        for i in range(vezes):
            matriz[i][vezes - 1 - i] = 3

        # Preenche o quadrado interno com 1
        inicio = vezes // 3
        fim = vezes - inicio

        for i in range(inicio, fim):
            for j in range(inicio, fim):
                matriz[i][j] = 1

        # Ponto central recebe 4
        centro = vezes // 2
        matriz[centro][centro] = 4


        for i in range(vezes):
            for j in range(vezes):
                print(matriz[i][j], end='')
            print()
        print()

    except EOFError:
        break
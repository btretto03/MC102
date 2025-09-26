while True:
    try:
        tam, vezes = map(int, input().split())
        vetor = input().split()

        posicoes = {}
        for i in range(tam):
            val = vetor[i]
            if val not in posicoes:
                posicoes[val] = []
            posicoes[val].append(i + 1)

        for _ in range(vezes):
            ocorrencia, elemento = input().split()
            ocorrencia = int(ocorrencia)

            if elemento in posicoes and len(posicoes[elemento]) >= ocorrencia:
                print(posicoes[elemento][ocorrencia - 1])
            else:
                print(0)

    except EOFError:
        break

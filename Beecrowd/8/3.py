while True:
    try:
        vezes = int(input())
        numeros = []
        for _ in range(vezes):
            num = input()      # se eu trabalhasse com num inteiros na hora de printar 0015 ele dava 15
            numeros.append(num)
        ordem = sorted(numeros)

        for i in ordem:
            print(i)

    except EOFError:
        break
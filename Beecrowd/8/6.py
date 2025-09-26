while True:
    try:
        hab, vezes = map(int, input().split())
        notas = []
        for _ in range(hab):
            nota = int(input())
            notas.append(nota)
        
        ordem = sorted(notas)
        for _ in range(vezes):
            posicao = int(input())
            print(ordem[-posicao])


    except EOFError:
        break

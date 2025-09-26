vezes = int(input())

for _ in range(vezes):
    N = int(input())

    numeros = input().split()

    carneirinhos = set()

    for i in range(N):
        carneirinhos.add(int(numeros[i]))

    print(len(carneirinhos))
    
while True:
    n = int(input())

    if n == 0:
        break

    m = 0 
    j = 0

    casos_totais = input().split()

    for i in casos_totais:
        if i == '0':
            m += 1
        elif i == '1':
            j += 1

    print(f"Mary won {m} times and John won {j} times")
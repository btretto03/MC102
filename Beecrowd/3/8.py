while True:
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a <= 0 or b <= 0:
        break

    lista = []
    lista.append(a)
    lista.append(b)
    a = min(lista)
    b = max(lista)

    x = 0
    for i in range(a,b+1):
        x += i
        print(i, end = " ")

    print(f"Sum={x}")
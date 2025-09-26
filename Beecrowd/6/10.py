vezes = int(input())

for _ in range(vezes):
    conjunto = set()
    itens = input().split(' ')
    for item in itens:
        conjunto.add(item)
    

    print(*sorted(conjunto))        
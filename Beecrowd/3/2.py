dias, saldo = input().split()
dias = int(dias)
saldo = int(saldo)
dift = []

i = 0
while i < dias:
    dep = int(input())
    saldo += dep
    dift.append(saldo)
    i += 1
diferenca = min(dift)
print(diferenca)
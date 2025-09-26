n = int(input())

i = 0
c = 0
r = 0
s = 0

while i < n:
    qnt, tipo = input().split()
    qnt = int(qnt)

    if tipo == 'C':
        c += qnt
    elif tipo == 'R':
        r += qnt
    elif tipo == 'S':
        s += qnt
    
    i += 1
total = c + s + r

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {c/ total * 100:.2f} %")
print(f"Percentual de ratos: {r / total * 100:.2f} %")
print(f"Percentual de sapos: {s / total * 100:.2f} %")
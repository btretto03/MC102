n, k = map(int, input(). split())

nomes = []
for _ in range(n):
    nome = input()
    nomes.append(nome)

chamada = sorted(nomes)

print(chamada[k - 1])

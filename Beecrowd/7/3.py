operacao = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

acima_diagonal_secundaria = []

for i in range(12):
    for j in range(12):
        if i + j < 11:
            acima_diagonal_secundaria.append(matriz[i][j])

if operacao == "M":
    media = sum(acima_diagonal_secundaria) / len(acima_diagonal_secundaria)
    print(f"{media:.1f}")

elif operacao == "S":
    soma = sum(acima_diagonal_secundaria)
    print(f"{soma:.1f}")
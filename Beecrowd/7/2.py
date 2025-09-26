operacao = input()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

acima_diagonal = []

for i in range(12):
    for j in range(12):
        if j > i:
            acima_diagonal.append(matriz[i][j])


if operacao == "M":
    media = sum(acima_diagonal) / len(acima_diagonal)
    print(f"{media:.1f}")

elif operacao == "S":
    soma = sum(acima_diagonal)
    print(f"{soma:.1f}")
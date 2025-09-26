def inverte(frase):
    resultado = ''
    y = len(frase) // 2

    for i in range(y - 1, -1, -1):  # Inverter a metade esquerda (da posição y-1 até 0)
        resultado += frase[i]

    for i in range(len(frase) - 1, y - 1, -1):   # Inverter a metade direita (da posição final até y)
        resultado += frase[i]

    return resultado


vezes = int(input())
for _ in range(vezes):
    frase = inverte(input())
    print(frase)
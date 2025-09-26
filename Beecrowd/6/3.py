skills, vezes = map(int, input().split())
dicionario = {}

for _ in range(skills):
    palavra, valor = input().split()
    dicionario[palavra] = int(valor)

for _ in range(vezes):
    salario = 0
    while True:
        linha = input()
        if linha == ".":
            break
        
        palavras = linha.split()
        for palavra in palavras:
            if palavra in dicionario:
                salario += dicionario[palavra]
    print(salario)
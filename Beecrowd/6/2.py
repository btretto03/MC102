def ordena(dicionario):
    ''' A funcao recebe um dicionario, pega suas chaves e ordena em ordem alfabetica
    depois crria uma lista com os pares (chave,valor) e a retorna'''
    chaves = list(dicionario.keys())
    chaves.sort() 
    itens_ordenados = []
    for chave in chaves:
        itens_ordenados.append((chave, dicionario[chave]))
    return itens_ordenados

def imprimir_percentuais(dicionario):
    total = sum(dicionario.values())
    ordenado = ordena(dicionario)
    for chave, valor in ordenado:
        percentual = (valor / total) * 100
        print(f"{chave} {percentual:.4f}")

vezes = int(input())
input() 

for i in range(vezes):
    arvores = {}
    while True:
        try:
            linha = input()
            if linha == '':
                break
            if linha not in arvores:
                arvores[linha] = 1
            else:
                arvores[linha] += 1
        except EOFError: # sem o erro estava dando Runtime error no beecrowdd
            break

    imprimir_percentuais(arvores)

    if i != vezes - 1: #separa com um espaço, menos na ultima vez
        print()
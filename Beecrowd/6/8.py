def escolhido(lista):
    '''A funcao recebe uma lista e devolve seu maior valor e em casa de empate o que apareceu primeiro
'''
    maior = ""
    for nome in lista:
        if len(nome) > len(maior):
            maior = nome
    return maior

nomes_sim = [] #usando lista nesse ja que o set nao guardaria a ordem que os elementos foram inseridos
nomes_nao = set()

while True:
    entrada = input()
    if entrada == "FIM":
        break

    nome, entra = entrada.split()
    if entra == "YES":
        if nome not in nomes_sim:
            nomes_sim.append(nome)
    else:
        nomes_nao.add(nome)

# Imprimir ordenados
for nome in sorted(nomes_sim):
    print(nome)
for nome in sorted(nomes_nao):
    print(nome)

print()
print(f"Amigo do Habay:\n{escolhido(nomes_sim)}")
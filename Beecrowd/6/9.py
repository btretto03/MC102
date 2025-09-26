qntlinguas = int(input())

tradutor = {}
for _ in range (qntlinguas):
    lingua = input()
    traducao = input()

    tradutor[lingua] = traducao  #lingua é a chave e traducao e o valor


qntcriancas = int(input())

for _ in range(qntcriancas):
    nome = input()
    lingua_nativa = input()

    print(nome)
    print(tradutor[lingua_nativa])
    print()  #beecrowd pede uma linha em branco após cada print



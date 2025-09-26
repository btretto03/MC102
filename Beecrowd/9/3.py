vezes = int(input())

z = int(input())
while z <= vezes:
    z = int(input())

soma = 0
contador = 0
atual = vezes

while soma <= z:
    soma += atual
    atual += 1
    contador += 1
print(contador)
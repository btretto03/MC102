pessoas = int(input())
codificadores = input().split()
numerosaidas = int(input())
saidas = input().split()

for numero in saidas:
    if numero in codificadores:
        codificadores.remove(numero)

print(*codificadores)

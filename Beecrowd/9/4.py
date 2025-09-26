def imprime_div(n, i=1):
    if i > n:
        return
    if n % i == 0:
        print(i)
    imprime_div(n, i + 1)

numero = int(input())
imprime_div(numero)
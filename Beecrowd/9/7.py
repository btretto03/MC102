def fracao(n):
    if n == 0:
        return 0
    return 1 / (2 + fracao(n - 1))

vezes = int(input())

aproximacao = 1 + fracao(vezes)
print(f"{aproximacao:.10f}")
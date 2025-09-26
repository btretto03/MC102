def soma_impares(a, b):
    '''
    A função pega um intervalo definido e soma a uma variável 
    inicialmente nula o valor de todos os primos que ali estão
    '''
    s = 0
    if a <= b:
        for i in range(a + 1, b):
            if i % 2 != 0:
                s += i
        return s
    else:
        for i in range(b + 1, a):
            if i % 2 != 0:
                s += i
        return s
    
vezes = int(input())

i = 0
while i < vezes:
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)

    soma = soma_impares(n1, n2)
    print(soma)

    i += 1
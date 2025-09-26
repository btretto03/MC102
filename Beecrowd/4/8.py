def fibonacci(a):
    '''A função recebe uma variável que representa a posição
    na sequência de fibonacci e, através de um laço vai adicionando
    valores na lista até chegar a essa posição para descobrir qual é o número
    '''
    lista = [0,1]
    global posicao
    j = 2
    while j <= posicao:
        x = lista[j-2]+lista[j-1]
        lista.append(x)
        j += 1
    fib = lista[posicao]
    print(f"Fib({posicao}) = {fib}")

vezes = int(input())

i = 0
while i < vezes:
    posicao = int(input())
    fibonacci(posicao)
    i += 1
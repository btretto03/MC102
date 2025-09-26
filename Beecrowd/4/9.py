def analisar (b,c):
    '''A função recebe dois valores e os analisa para saber o comportamento das raízes da função;
    como sabemos que b e c são maiores que 0 já que são um valor positivo multiplicado por um módulo,
    não precisamos analisar todos os casos da biquadrada'''
    if b == 0 and c == 0:
        print("Bom")
    elif b != 0 and c == 0:
        print("So o ouro")
    elif b == 0 and c != 0:
        print("So o ouro")
    elif b != 0 and c != 0:
        print("So o ouro")


while True:
    n = int(input())
    if n == -1:
        break

    b = n % 257
    c = n % 193

    analisar(b,c)


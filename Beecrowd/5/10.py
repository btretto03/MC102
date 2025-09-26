def varia(num, palavra):
    '''A função recebe uma palavra e um numero e devolve cada digito da palavra com a variacao do numero pedida'''

    lista = []
    for letra in palavra:
        if (ord(letra) - num) >= 65:
            letranova = chr(ord(letra) - num)
            lista.append(letranova)
        else:
            letranova = chr(ord(letra) - num + 26)
            lista.append(letranova)

    print(*lista,sep ='')


vezes = int(input())

for i in range(vezes):
    palavra = input()
    num = int(input())
    varia(num, palavra)

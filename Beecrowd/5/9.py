def confere(num1,num2):
    '''A função recebe dois números(strings) e confere se os últimos algarismos deles 
    '''

    for i in range(1, len(num2) + 1):
        if len(num1) < len(num2):
            return False
        if num2[-i] != num1[-i]:
            return False
    return True
        
        
vezes = int(input())

for _ in range(vezes):
    num1, num2 = input().split()

    if confere(num1, num2) == True:
        print("encaixa")
    else:
        print("nao encaixa")
    
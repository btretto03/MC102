vezes = int(input())

for _ in range(vezes):
    frase = input().split()
    if frase == []:  
        print()
        continue 

    i = 0
    palavra = []
    for i in range(len(frase)):
        palavra.append(frase[i][0])
        
    print(''.join(palavra))
vezes = int(input())

for _ in range(vezes):
    num = input()
    if len(num) == 5:
        print("3")
    elif num[0] == "o" or num[2] == "e": 
        print("1")
    elif num[0] == "t" or num[2] == "o":
        print("2")

    #Podemos considerar o ou entre a primeira e a ultima letra no caso do one e do two, já que só pode errar uma letra e, se uma está errada
    #a outra necessariamente está correta

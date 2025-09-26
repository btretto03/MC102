vezes = int(input())

for _ in range(vezes):
    num = input()
    cont = 0
    
    for i in num:
        if i == "1":
            cont += 2
        elif i == "7":
            cont += 3
        elif i == "4":
            cont += 4
        elif i == "2" or i == "5" or i == "3":
            cont += 5
        elif i == "0" or i == "9" or i == "6":
            cont += 6
        elif i == "8":
            cont += 7

    print(f"{cont} leds")
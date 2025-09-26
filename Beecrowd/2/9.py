pay = float(input())

if pay <= 400:
    add = 0.15*pay
    print(f"Novo salario: {pay + add:.2f}")
    print(f"Reajuste ganho: {add:.2f}")
    print(f"Em percentual: 15 %")

elif pay <=800:
    add = 0.12*pay
    print(f"Novo salario: {pay + add:.2f}")
    print(f"Reajuste ganho: {add:.2f}")
    print(f"Em percentual: 12 %")

elif pay <=1200:
    add = 0.10*pay
    print(f"Novo salario: {pay + add:.2f}")
    print(f"Reajuste ganho: {add:.2f}")
    print(f"Em percentual: 10 %")

elif pay <=2000:
    add = 0.07*pay
    print(f"Novo salario: {pay + add:.2f}")
    print(f"Reajuste ganho: {add:.2f}")
    print(f"Em percentual: 7 %")

elif pay > 2000:
    add = 0.04*pay
    print(f"Novo salario: {pay + add:.2f}")
    print(f"Reajuste ganho: {add:.2f}")
    print(f"Em percentual: 4 %")
    
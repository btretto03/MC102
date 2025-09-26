pay = float(input())

if pay <= 2000.00:
    print("Isento")

elif pay <= 3000.00:
    pay2 = (pay - 2000)*0.08
    print(f"R$ {pay2:.2f}")

elif pay <= 4500.00:
    pay3 = 80.00 + (pay - 3000)*0.18
    print(f"R$ {pay3:.2f}")

elif pay > 4500.00:
    pay4 = 350.00 + (pay - 4500)*0.28
    print(f"R$ {pay4:.2f}")
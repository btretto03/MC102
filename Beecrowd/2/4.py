c1, c2 = input().split()
c1= int(c1)
c2= int(c2)

if c1 == 1:
    c1 = float(4.00)

elif c1 == 2:
    c1 = float(4.50)

elif c1 == 3:
    c1 = float(5.00)

elif c1 == 4:
    c1 = float(2.00)

elif c1 == 5:
    c1 = float(1.50)


total = c1*c2

print(f"Total: R$ {total:.2f}")
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

#Delta:
d = b**2 - 4*a*c

if d < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + d**0.5)/2/a
    r2 = (-b - d**0.5)/2/a
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
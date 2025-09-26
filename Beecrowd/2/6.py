a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

#Vamos adotar o x como maior lado do triângulo:
if a >= b and a >= c:
    x = a
    y = b
    z = c

if b >= a and b >= c:
    x = b
    y = a
    z = c

if c >= a and c >= b:
    x = c
    y = a
    z = b

#Caso 1
if x >= y + z:
    print("NAO FORMA TRIANGULO")

#Caso 2
elif x**2 == y**2 + z**2:
    print("TRIANGULO RETANGULO")

#caso 3
elif x**2 > y**2 + z**2:
    print("TRIANGULO OBTUSANGULO")

#caso 4
elif x**2 < y**2 + z**2:
    print("TRIANGULO ACUTANGULO")

#casos especiais
if x == y  and y == z:
    print("TRIANGULO EQUILATERO")
elif x == y or x == z or y ==z:
    print("TRIANGULO ISOSCELES")
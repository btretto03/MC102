num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())

soma = 0
positivos = 0

if num1>0:
    soma +=num1
    positivos += 1

if num2>0:
    soma +=num2
    positivos += 1


if num3>0:
    soma +=num3
    positivos += 1


if num4>0:
    soma +=num4
    positivos += 1


if num5>0:
    soma +=num5
    positivos += 1
    
if num6>0:
    soma +=num6
    positivos += 1


print(f"{positivos} valores positivos")
print(f"{soma/positivos :.1f}")
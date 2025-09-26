i = 0
positivos = 0

while i < 6:
    i += 1
    x = float(input())
    if x > 0:
        positivos += 1

print(f"{positivos} valores positivos")
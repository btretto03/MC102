qnt = int(input())

i = 0
l = []

while i < qnt:
    latas, copos = input().split()
    latas = int(latas)
    copos = int(copos)
    if latas > copos:
        l.append(copos)
    i += 1
    
copos_quebrados = sum(l)
print(copos_quebrados)
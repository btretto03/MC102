n = int(input())

if 0<n<=13:
    i = n-1
    while i > 0 :
        n = n*i
        i -= 1
print(f"{n}")
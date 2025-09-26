N=int(input())

a=int(N//3600)
b=(N-a*3600)//60
c=N%60
print(f"{a}:{b}:{c}")
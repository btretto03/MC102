N=int(input())
print(f"{N}")

#notas de 100:
a=N//100
print(f"{a:.0f} nota(s) de R$ 100,00")

#notas de 50:
b=(N-a*100)//50
print(f"{b:.0f} nota(s) de R$ 50,00")

#notas de 20:
c=(N-a*100-b*50)//20
print(f"{c:.0f} nota(s) de R$ 20,00")

#notas de 10:
d=(N-a*100-b*50-c*20)//10
print(f"{d:.0f} nota(s) de R$ 10,00")

#notas de 5:
e=(N-a*100-b*50-c*20-d*10)//5
print(f"{e:.0f} nota(s) de R$ 5,00")

#notas de 2:
g=(N-a*100-b*50-c*20-d*10-5*e)//2
print(f"{g:.0f} nota(s) de R$ 2,00")


#Notas de 1:
h=(N-a*100-b*50-c*20-d*10-5*e-2*g)//1
print(f"{h:.0f} nota(s) de R$ 1,00")


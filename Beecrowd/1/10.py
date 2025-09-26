N=float(input())

print(f"NOTAS:")

#notas de 100:
a=N//100
print(f"{a:.0f} nota(s) de R$ 100.00")

#notas de 50:
b=(N-a*100)//50
print(f"{b:.0f} nota(s) de R$ 50.00")

#notas de 20:
c=(N-a*100-b*50)//20
print(f"{c:.0f} nota(s) de R$ 20.00")

#notas de 10:
d=(N-a*100-b*50-c*20)//10
print(f"{d:.0f} nota(s) de R$ 10.00")

#notas de 5:
e=(N-a*100-b*50-c*20-d*10)//5
print(f"{e:.0f} nota(s) de R$ 5.00")

#notas de 2:
g=(N-a*100-b*50-c*20-d*10-5*e)//2
print(f"{g:.0f} nota(s) de R$ 2.00")

print(f"MOEDAS:")

#Moedas de 1:
h=(N-a*100-b*50-c*20-d*10-5*e-2*g)//1
print(f"{h:.0f} moeda(s) de R$ 1.00")

i=int(round(100*(N-N//1),0))

#Moedas de 50:
j=i//50
print(f"{j:.0f} moeda(s) de R$ 0.50")

#Moedas de 25:
k=(i-j*50)//25
print(f"{k:.0f} moeda(s) de R$ 0.25")

#Moedas de 10:
l=(i-j*50-k*25)//10
print(f"{l:.0f} moeda(s) de R$ 0.10")


#Moedas de 5:
m=(i-j*50-k*25-l*10)//5
print(f"{m:.0f} moeda(s) de R$ 0.05")

#Moedas de 1:
n=(i-j*50-k*25-l*10-m*5)//1
print(f"{n:.0f} moeda(s) de R$ 0.01")
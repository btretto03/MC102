Nota1, Nota2, Nota3, Nota4 = input().split()

Nota1 = float(Nota1)
Nota2 = float(Nota2)
Nota3 = float(Nota3)
Nota4 = float(Nota4)

med = float((Nota1*2 + Nota2*3 + Nota3*4 + Nota4)/10)
print(f"Media: {med:.1f}")

if med >=7:
    print('Aluno aprovado.')

elif med < 5:
    print("Aluno reprovado.")

elif med >= 5 and med < 7:
    print("Aluno em exame.")
    
    Exame = float(input())
    print(f"Nota do exame: {Exame:.1f}")
    Notaf = float(( Exame + med)/2)
    
    if Notaf >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {Notaf:}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {Notaf}")
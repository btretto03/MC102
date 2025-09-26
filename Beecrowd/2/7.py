t1, t2 = input().split()

t1 = int(t1)
t2 = int(t2)
t3 = 24 - t1

#Jogo começa e termina no mesmo dia
if t2 > t1:
    print(f"O JOGO DUROU {t2 - t1} HORA(S)")

#jogo em dia diferente:
elif t1>t2:
    print(f"O JOGO DUROU {t2 + t3} HORA(S)")

#jogo dura um dia:
elif t1 == t2:
    print("O JOGO DUROU 24 HORA(S)")
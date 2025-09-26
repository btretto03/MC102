while True:

    a, b = input().split()
    a = int(a)
    b = int(b)
    
    if a == 0 and b == 0:
        break
    
    ingressos = input().split()
    ing = set(ingressos)
    rep = []

    cont = 0
    for i in ing:
        if(ingressos.count(i) > 1):
            cont += 1
            rep.append(i)
    print(cont)
    
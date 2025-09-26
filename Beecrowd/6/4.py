vezes = int(input())

for _ in range(vezes):
    produtosfeira = int(input())
    listafeira = {} 
    for _ in range (produtosfeira):
        prod, preco = input().split()
        preco = float(preco)
        listafeira[prod] = preco

    comprar = int(input())

    valorgasto = 0
    for _ in range(comprar):
        prod2, qnt = input().split()
        qnt = int(qnt)

        if prod2 in listafeira:
            valorgasto += (listafeira[prod2])*qnt

    print(f"R$ {valorgasto:.2f}")


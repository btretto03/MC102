while True: 
    try:
        texto = input()
        lista = []

        for j in texto:
            lista.append(j)

        frequencias = {}
        ja_feito = set()
        for letra in lista:
            if letra not in ja_feito:
                count = 0
                i = 0
                for i in range(len(lista)):
                    if letra == lista[i]:
                        count += 1
                    i += 1
                ja_feito.add(letra)
                frequencias[letra] = count
        frequencias_ordem = []
        for chave in frequencias:
            frequencias_ordem.append( (frequencias[chave], -ord(chave), chave) )

        frequencias_ordem.sort()

        for freq, neg_ascii, chave in frequencias_ordem:
            print(ord(chave), freq)

    except EOFError:
        break
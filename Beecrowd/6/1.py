palavras_distintas = set() #set ja que nao aceita elementos repetidos

while True:
    try:
        texto = input()
        palavra = ''

        for letra in texto:
            letramin = letra.lower()
            if 97 <= ord(letramin) <= 122:  # letras de a-z
                palavra += letramin
            else:
                if palavra != '':
                    palavras_distintas.add(palavra)
                    palavra = ''
        if palavra != '':
            palavras_distintas.add(palavra)

    except EOFError:
        break

for palavra in sorted(palavras_distintas):
    print(palavra)

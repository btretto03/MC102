c1 = input()
c2 = input()
c3 = input()

if c1 == "vertebrado" and c2 == "ave":
    if c3 == "carnivoro":
        print("aguia")
    if c3 == "onivoro":
        print("pomba")

if c1 == "vertebrado" and c2 == "mamifero":
    if c3 == "herbivoro":
        print("vaca")
    if c3 == "onivoro":
        print("homem")

if c1 == "invertebrado" and c2 == "inseto":
    if c3 == "hematofago":
        print("pulga")
    if c3 == "herbivoro":
        print("lagarta")

if c1 == "invertebrado" and c2 == "anelideo":
    if c3 == "hematofago":
        print("sanguessuga")
    if c3 == "onivoro":
        print("minhoca")
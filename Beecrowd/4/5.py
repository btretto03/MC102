def ano_bissexto(ano):
    """
    A função recebe um ano e de acordo com parâmetros dados no enunciado avalia
    se o ano é bissexto ou não, retornando true(bissexto) ou false(não)
    """

    if ano % 400 == 0:
        return True
    elif ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False

def dias_desde_ano1(ano, mes, dia):
    """
    A função recebe  uma data e devolve quantos dias passaram a partir de um dado 
    referencial(1970)
    """
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_dias = 0
    for a in range(1970, ano):
        if ano_bissexto(a):
            total_dias += 366
        else:
            total_dias += 365

    for m in range(1, mes):
        if m == 2 and ano_bissexto(ano):
            total_dias += 29
        else:
            total_dias += dias_mes[m - 1]

    total_dias += dia

    return total_dias


vezes = int(input())

for _ in range(vezes):
    data1, data2 = input().split()
    ano1, mes1, dia1 = map(int, data1.split('-')) #pesquisei como fazia pra transformar cada parte da data em inteiro
    ano2, mes2, dia2 = map(int, data2.split('-'))

    dias1 = dias_desde_ano1(ano1, mes1, dia1)
    dias2 = dias_desde_ano1(ano2, mes2, dia2)

    print(abs(dias1 - dias2))
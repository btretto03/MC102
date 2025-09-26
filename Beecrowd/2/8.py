#hr=hora, min= minuto, i = inicial, f = final

hri, mini, hrf, minf = input().split()
hri = int(hri)
mini = int(mini)
hrf = int(hrf)
minf = int(minf)

horastotais = hrf - hri
if hrf < hri:
    horastotais += 24

mintotais = minf - mini

if minf < mini:
    mintotais += 60
    horastotais -=1
    if horastotais < 0:
        horastotais +=24

if hrf == hri  and minf == mini:
    horastotais = 24

print(f"O JOGO DUROU {horastotais} HORA(S) E {mintotais} MINUTO(S)")
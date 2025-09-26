while True:
    try:
        N = int(input())
        nomes = []
        criancas_mais = 0
        criancas_menos = 0
        
        for _ in range(N):
            sinal, nome = input().split()                     
            nomes.append(nome) 
            
            if sinal == '+':
                criancas_mais += 1
            else:
                criancas_menos += 1
                
        nomes_ordenados = sorted(nomes) 
        

        for nome_crianca in nomes_ordenados:
            print(nome_crianca)
            
    
        print(f"Se comportaram: {criancas_mais} | Nao se comportaram: {criancas_menos}")
        
    except EOFError:
        break 
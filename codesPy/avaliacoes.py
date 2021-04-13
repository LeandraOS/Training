def verificaDesempenho(atividade, km, tempo):
    km_total = km / tempo
    if atividade == 1:
        desempenhoCorrida(km_total)
    else:
        desempenhoPedal(km_total)

def desempenhoCorrida(km_total):
    if (km_total > 10):
        print ("Desempenho excelente")
    elif (km_total >= 5 and km_total <= 15):
        print ("Desempenho médio")
    elif (km_total < 5):
        print("Baixo desempenho")
    elif (km_total > 12):
        print("Desempenho excelente")

def desempenhoPedal(km_total):
    if (km_total > 24):
        print ("Desempenho excelente")
    elif (km_total >= 10 and km_total <= 24):
        print ("Desempenho médio")
    elif (km_total < 10):
        print("Baixo desempenho")
    elif (km_total > 20):
        print("Desempenho excelente")

verificaDesempenho(1, 5, 0.5)
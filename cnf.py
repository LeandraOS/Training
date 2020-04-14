#coding: utf-8

quantidade = int(input())
qtd_validas = 0
clausulas = []
atomos = []
resultado = []

def temLiteraisComplementares(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)):
            if lista[i] == ("!" + lista[j]):
                return True
            elif("!" + lista[i]) == lista[j]:
                return True
    return False
            
for i in range(quantidade):
    clausulas = input().lower().split("&")
    for j in range (len(clausulas)):
        atomos = clausulas[j].replace("(","").replace(")","").split("|")
    if temLiteraisComplementares(atomos) == True:
        resultado.append("eh valido")
    else:
        resultado.append("não eh válido")

for result in range(len(resultado)):
    print(resultado[result])

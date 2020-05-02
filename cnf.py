#coding: utf-8

def ehValida(lista):
    for i in range(len(lista)):
        if lista[0] == "!":
             if (lista[i] in lista):
                return True
        else:
            if ("!"  +  lista [i]) in lista:
                return True
            
    return False

qtd_formulas = int(input())
clausulas = []
atomos = set()

for i in range(qtd_formulas):
    clausulas = input().replace(' ', '').lower().split("&")
    for j in range (len(clausulas)):
        atomos = clausulas[j].replace("(","").replace(")","").split("|")
    if ehValida(atomos):
        print("eh valida")
    else:
        print("não eh válida")



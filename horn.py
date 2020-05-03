#coding: utf-8

atomos_separados = {}

qtd_formulas = int(input())
contador_de_formulas = 0
separada = list()
false = "F"


for i in range(qtd_formulas):
    formulas = input().replace(' ', '').lower().split("&")
    for j in range(len(formulas)):
        separada.append(formulas[j].replace("(","").replace(")",""))
    if (false.lower() not in separada):
        print ("{}.satisfazível".format(i + 1))
    else:
        
print(separada)
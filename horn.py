#coding: utf-8

atomos_separados = {}

qtd_formulas = int(input())
separada = list()
false = "F"

for i in range(qtd_formulas):
    formulas = input().replace(' ', '').lower().split("&")
    if (false.lower() not in formulas):
        print("{}.satisfazível".format(i + 1))
    else:
        for j in range(len(formulas)):
            separada.append(formulas[j].replace("(","").replace(")",""))
        #verificacao de quando a formula nao eh satisfazivel
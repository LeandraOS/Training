#coding: utf-8

def separa_em_Atomos(formula):
  atomos = []
  for l in formula:
    if l.isalpha() and (l not in atomos):
      atomos.append(l)
  return atomos;

def satisfazivel(formula):  
  satisfazivel = True

  if 'F' not in separa_em_Atomos(formula):
    return satisfazivel

  atomos_checados = ['T']
  formula = formula.replace(' ', '')
  subformulas = formula[1:len(formula)-1].split(')&(')
  print(subformulas)
  checado = False
  i = 0

  while(i < len(subformulas)):
    sem_implicacao = subformulas[i].split('->')
    atomos_da_esquerda = separa_em_Atomos(sem_implicacao[0])

    if set(atomos_da_esquerda).intersection(atomos_checados):
      if sem_implicacao[1] not in atomos_checados:
           atomos_checados.append(sem_implicacao[1])
           checado = True

      else:
        checado = False

    i+=1
    
    if checado and i >= len(subformulas):
      checado = False 
      i = 0
  
  if 'F' in atomos_checados:
    satisfazivel = False

  return satisfazivel

qtd_entrada = int(input('Entradas: '))

for i in range(qtd_entrada):
  formula = input('Formula ' + str(i + 1) + ': ')  

  if(satisfazivel(formula)):
    print(str(i+1) + '.Satisfazível')

  else:
    print(str(i+1) + '.Insatisfazível')
  
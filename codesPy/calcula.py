def dobro(num):
  return num * 2

def CalculaQtdDiasInfeccao(numPessoas, populacao):
  qtdPessoas = 0
  dias = 0
  while (qtdPessoas <= populacao):
    qtdPessoas =  numPessoas + dobro(qtdPessoas)
    numPessoas = qtdPessoas
    if (qtdPessoas <= populacao):
      dias += 3

  print (dias)

CalculaQtdDiasInfeccao(2,100)
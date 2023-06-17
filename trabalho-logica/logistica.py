from ast import Return
#Início da função dimensoesObjeto()
def dimensoesObjeto():
  print('-------------------- Tabela 1/3 - Dimensões --------------------')
  while True:
    try:
      altura = int(input('Digite a altura do objeto (cm): '))
      comprimento = int(input('Digite o comprimento do objeto (cm): '))
      largura = int(input('Digite a largura do objeto (cm): '))
      dimensoes = (altura * comprimento * largura)
      print('A dimensão do objeto:', dimensoes ,'cm')
      if (dimensoes < 1000):
        return 10
      elif (1000 <= dimensoes < 10000):
        return 20
      elif (10000 <= dimensoes < 30000):
        return 30
      elif (30000 <= dimensoes < 100000):
        return 50
      else:
        (dimensoes >= 100000)
        print('Dimensões iguais ou acima de 100000 não são aceitas!')
        print('Por favor, insira os dados novamente.')
    except ValueError:
      print('Pare de digitar caracteres não numéricos!')
      print('Por favor, insira os dados novamente.')
#Fim da função dimensoesObjeto()

#Início da função pesoObjeto()
def pesoObjeto():
  print('----------------------- Tabela 2/3 - Peso ----------------------')
  while True:
    try:
      peso = float(input('Digite o peso do objeto (kg): '))
      if (peso <= 0.1):
        return 1
      elif (0.1 <= peso < 1):
        return 1.5
      elif (1 <= peso < 10):
        return 2
      elif (10 <= peso < 30):
        return 3
      else:
        (peso >= 30)
        print('Pesos iguais ou acima de 30kg não são aceitos!')
    except ValueError:
      print('Pare de digitar caracteres não numéricos!')
      print('Por favor, insira os dados novamente.')
#Fim da função pesoObjeto()

#Início da função rotaObjeto()
def rotaObjeto():
  print('----------------------- Tabela 3/3 - Rota ----------------------')
  while True:
    rota = input('Qual será a rota utilizada? (use as siglas) \n' +
                    'rs - De Rio de Janeiro até São Paulo \n' +
                    'sr - De São Paulo até Rio de Janeiro \n' +
                    'bs - De Brasília até São Paulo \n' +
                    'sb - De São Paulo até Brasília \n' +
                    'br - De Brasília até Rio de Janeiro \n' +
                    'rb - De Rio de Janeiro até Brasília \n' +
                    '>> ')
    if rota == 'rs':
      return 1
    elif rota == 'sr':
      return 1
    elif rota == 'bs':
      return 1.2
    elif rota == 'sb':
      return 1.2
    elif rota == 'br':
      return 1.5
    elif rota == 'rb':
      return 1.5
    else:
      print('Rota não encontrada, digite uma rota válida!')
      continue
    break
#Fim da função rotaObjeto()

#Início do Main
print('---- Bem-vindo a Logística do Yuri ----')
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print('(Dimensões: {} * Peso: {} * Rota: {})'.format(dimensoes, peso, rota))
print('Total a pagar: R${:.2f}'.format(total))
#----------------- Início das Variáveis Globais -----------------
listaPeca = []
codigoPeca = 0
#------------------ Fim das Variáveis Globais -------------------

#------------------ Início de cadastrarPeca() -------------------
def cadastrarPeca(codigo):
  print('-------------------------------------------------------------------------------------')
  print('|                      Bem-vindo ao menu de Cadastrar Peça                          |')
  print('-------------------------------------------------------------------------------------')
  print('Código da peça: {}'.format(codigo))
  nome = input ('Digite o NOME da peça: ')
  fabricante = input ('Digite o FABRICANTE da peça: ')
  preco = int(input ('Digite o PREÇO(R$) da peça: '))
  dicionarioPeca = {'codigo'     : codigo,
                    'nome'       : nome,
                    'fabricante' : fabricante,
                    'preco'      : preco}
  listaPeca.append(dicionarioPeca.copy())
#------------------- Fim de cadastrarPeca() ---------------------

#------------------ Início de consultarPeca() -------------------
def consultarPeca():
  print('-------------------------------------------------------------------------------------')
  print('|                          Bem-vindo ao menu de Consultar Peça                      |')
  print('-------------------------------------------------------------------------------------')
  while True:
    opcao_consultar = input('\nEscolha a opção desejada:\n'+
                            '1-Consultar TODAS as Peças\n'+
                            '2-Consultar Peças por CÓDIGO\n'+
                            '3-Consultar Peças por FABRICANTE\n'+
                            '4-Retornar\n'+
                            '>> ')
    if opcao_consultar == '1':
      print('Você escolheu a opção Consultar TODAS as Peças')
      for peca in listaPeca: #peca vai varrer toda a lista de produtos
        print('------------------------------')
        for key, value in peca.items(): #Varrer todos os conjuntos chave e valor do dicionário peca
          print('{}: {}'.format(key,value))
        print('------------------------------')
    elif opcao_consultar == '2':
      print('Você escolheu a opção Consultar Peças por CÓDIGO')
      codigoDesejado = int(input('Digite o CÓDIGO desejado: '))
      for peca in listaPeca:
        if peca['codigo'] == codigoDesejado: #O valor do campo código desse dicionário é igual o código desejado
          print('------------------------------')
          for key, value in peca.items(): #Varre todos os conjuntos chave e valor do dicionario peca
            print('{}: {}'.format(key,value))
        print('------------------------------')
    elif opcao_consultar == '3':
      print('Você escolheu a opção Consultar Peças por FABRICANTE')
      codigoDesejado = input('Digite o FABRICANTE desejado: ')
      for peca in listaPeca:
        if peca['fabricante'] == codigoDesejado: #O valor do campo código desse dicionário é igual o código desejado
          print('------------------------------')
          for key, value in peca.items(): #Varre todos os conjuntos chave e valor do dicionario peca
            print('{}: {}'.format(key,value))
        print('------------------------------')
    elif opcao_consultar == '4':
      return #Sai de consultarPeca e volta para Main
    else:
      print('Opção Inválida. Tente Novamente!')
      continue #Volta para o início de consultarPeca
#------------------- Fim de consultarPeca() ---------------------

#------------------- Início de removerPeca() --------------------
def removerPeca():
  print('-------------------------------------------------------------------------------------')
  print('|                         Bem-vindo ao menu de Remover Peça                         |')
  print('-------------------------------------------------------------------------------------')
  codigoDesejado = int(input('Digite o CÓDIGO da peça que deseja remover: '))
  for peca in listaPeca:
    if peca['codigo'] == codigoDesejado:
      listaPeca.remove(peca)
      print('>> PEÇA REMOVIDA <<')
#-------------------- Fim de removerPeca() ----------------------

#------------------------ Início de Main ------------------------
print('-------------------------------------------------------------------------------------')
print('|              Bem-vindo ao Controle de Estoque da Bicicletaria do Yuri             |')
print('-------------------------------------------------------------------------------------')
while True:
  opcao_principal = input('\nEscolha a opção desejada: \n'+
                          '1-Cadastrar Peça\n'+
                          '2-Consultar Peça\n'+
                          '3-Remover Peça\n'+
                          '4-Sair\n'+
                          '>> ')
  if opcao_principal == '1':
    codigoPeca = codigoPeca + 1
    cadastrarPeca(codigoPeca)
  elif opcao_principal == '2':
    consultarPeca()
  elif opcao_principal == '3':
    removerPeca()
  elif opcao_principal == '4':
    print('>> PROGRAMA FINALIZADO <<')
    break #Encerra o laço principal e o programa finaliza
  else:
    print('Opção Inválida. Tente Novamente!')
    continue #Volta para o início do Main
#------------------------- Fim de Main --------------------------
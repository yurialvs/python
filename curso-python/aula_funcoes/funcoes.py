# ********************************************************************************** #

# DICA PARA CRIAR FUNÇÃO

# def <identificador da funcao> (<parametro(s)>):
# 	<código que será executado>
# 	return <Dado que será retornado, caso seja necessário>

# As funções representam "ações" como: inserir, exibir, consultar, apagar, calcular

# ********************************************************************************** #

# FUNÇÕES PARA LISTAS NÚMERICAS

# # Cria listas vazias para armazenamento
# valores = []
# inventario = []

# resposta = 'S'

# # Adiciona um equipamento
# while resposta == 'S':
#     equipamento = [input('Digite o nome do Equipamento: '), # Indice[0]
#                 float(input('Valor: ')),                    # Indice[1]
#                 int(input('Número Serial: ')),              # Indice[2]
#                 input('Departamento: ')]                    # Indice[3]
#     inventario.append(equipamento)
#     resposta = input('Digite "S" para continuar: ').upper()
#     print('____________________________')

# # Lista de Equipamentos
# for elemento in inventario:
#     print('Nome.........: ', elemento[0])
#     print('Valor........: ', elemento[1])
#     print('Serial.......: ', elemento[2])
#     print('Departamento.: ', elemento[3])
#     print('____________________________')

# # Adiciona os valores dos equipamentos no indice[1]
# for elemento in inventario:
#     valores.append(elemento[1])

# # Busca e verifica os valores
# if len(valores) > 0:
#     print('O equipamento mais caro custa: ', max(valores)) # max(valores) retorna o maior valor
#     print('O equipamento mais barato custa: ', min(valores)) # min(valores) retorna o menor valor
#     print('O total de equipamentos é de: ', sum(valores)) # sum(valores) retorna a soma de todos

# --------------------------------------------------------------------------------- #

def preencherInventario(lista):
    resp = 'S'
    while resp.strip().upper() == 'S':
        equipamento = [input('Digite o nome do Equipamento: '),
                       float(input('Valor: ')),
                       int(input('Número Serial: ')),
                       input('Departamento: ')]
        lista.append(equipamento)
        resp = input('Digite "S" para continuar: ')

def exibirInventario(lista):
    for elemento in lista:
        print('Nome..........: ', elemento[0])
        print('Valor.........: ', elemento[1])
        print('Serial........: ', elemento[2])
        print('Departamento..: ', elemento[3])

def localizarPorNome(lista):
    busca = input('Digite o NOME do equipamento que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
                print('Valor.........: ', elemento[1])
                print('Serial........: ', elemento[2])

def depreciarPorNome(lista, porc):
     depreciacao = input('Digite o NOME do equipamento que será depreciado: ')
     for elemento in lista:
          if depreciacao == elemento[0]:
               print('Valor antigo: ', elemento[1])
               elemento[1] = elemento[1] * (1-porc/100)
               print('Novo valor: ', elemento[1])

def excluirPorSerial(lista):
    serial = int(input('Digite o serial do equipamento que será excluído: '))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return 'Itens excluídos.'  

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print('O equipamento mais caro custa: ', max(valores)) # max(valores) retorna o maior valor
        print('O equipamento mais barato custa: ', min(valores)) # min(valores) retorna o menor valor
        print('O total de equipamentos é de: ', sum(valores)) # sum(valores) retorna a soma de todos

# --------------------------------------------------------------------------------- #

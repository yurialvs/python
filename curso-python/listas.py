# # Lista vazia
# lista_vazia = []

# # Lista preenchida estaticamente
# lista_estatica = ['xpto', True]

# # Lista preenchida dinamicamente
# lista_dinamica = [input('Digite o usuário: '), bool(int(input('Está logado? ')))]

# --------------------------------------------------------------------------------- #

# ADICIONANDO DADOS EM UMA LISTA DE MANEIRA INDETERMINADA

# inventario = []
# resposta = 'S'
# while resposta == 'S':
#     inventario.append(input('Equipamento: '))
#     inventario.append(float(input('Valor: ')))
#     inventario.append(int(input('Número Serial: ')))
#     inventario.append(input('Departamento: '))
#     resposta = input('Digite "S" para continuar: ').upper()

# for elemento in inventario:
#     print(inventario)

# --------------------------------------------------------------------------------- #

# MÚLTIPLAS LISTAS

# # Cria equipamentos
# equipamentos = []
# valores = []
# seriais = []
# departamentos = []
# resposta = "S"
# while resposta == "S":
#   equipamentos.append(input("Equipamento: "))
#   valores.append(float(input("Valor: ")))
#   seriais.append(int(input("Número Serial: ")))
#   departamentos.append(input("Departamento: "))
#   resposta = input('Digite "S" para continuar: ').upper()

# # Lista os equipamentos
# for indice in range(0,len(equipamentos)):
#   print("Equipamento..: ", (indice+1))
#   print("Nome.........: ", equipamentos[indice])
#   print("Valor........: ", valores[indice])
#   print("Serial.......: ", seriais[indice])
#   print("Departamento.: ", departamentos[indice])

# # Busca equipamentos
# busca = input('Digite o nome do equipamento que deseja buscar: ')
# for indice in range(0, len(equipamentos)):
#   if busca == equipamentos[indice]:
#     print('Valor..: ', valores[indice])
#     print('Serial.: ', seriais[indice])

# # Altera valor dos equipamentos
# depreciacao = input('Digite o nome do equipamento que será depreciado: ')
# for indice in range(0, len(equipamentos)):
#   if depreciacao == equipamentos[indice]:
#     print('Valor antigo: ', valores[indice])
#     valores[indice] = valores[indice] * 0.9
#     print('Novo valor: ', valores[indice])

# # Remove equipamentos
# serial = int(input('Digite o serial do equipamento que será excluido: '))
# for indice in range(0, len(departamentos)):
#   if seriais[indice] == serial:
#     del departamentos[indice]
#     del equipamentos[indice]
#     del seriais[indice]
#     del valores[indice]
#     break

# # Lista os equipamentos
# for indice in range(0, len(equipamentos)):
#   print('Equipamento..: ', (indice + 1))
#   print('Nome.........: ', equipamentos[indice])
#   print('Valor........: ', valores[indice])
#   print('Serial.......: ', seriais[indice])
#   print('Departamento.: ', departamentos[indice])

# --------------------------------------------------------------------------------- #

# LISTAS DENTRO DE LISTAS


# --------------------------------------------------------------------------------- #

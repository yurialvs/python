# # Lista vazia
# lista_vazia = []

# # Lista preenchida estaticamente
# lista_estatica = ['xpto', True]

# # Lista preenchida dinamicamente
# lista_dinamica = [input('Digite o usuário: '), bool(int(input('Está logado? ')))]

# --------------------------------------------------------------------------------- #

# ADICIONANDO DADOS EM UMA LISTA DE MANEIRA INDETERMINADA

inventario = []
resposta = 'S'
while resposta == 'S':
    inventario.append(input('Equipamento: '))
    inventario.append(float(input('Valor: ')))
    inventario.append(int(input('Número Serial: ')))
    inventario.append(input('Departamento: '))
    resposta = input('Digite "S" para continuar: ').upper()
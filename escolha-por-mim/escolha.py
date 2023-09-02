import random

# Opções
print('Olá, seja bem-vindo ao Python Selector!')
opcao1 = input('Digite a primeira opção: ')
opcao2 = input('Digite a segunda opção: ')

# Use o random.choice para selecionar aleatoriamente alguma opção

opcao_selecionada = random.choice([opcao1, opcao2])

# Exiba a opção selecionada

print('Python escolheu: ', opcao_selecionada)
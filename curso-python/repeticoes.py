# LAÇO WHILE
# Faz contagem do número desejado até 99

# numero = int(input('Digite um número: '))
# while numero < 100:
#     print('' + str(numero))
#     numero = numero + 1
# print('Laço encerrado...')

# --------------------------------------------------------------------------------- #

# LAÇO FOR
# Faz contagem até um número antes do número desejado

# for numero in range(1, int(input('Digite um número para determinar o fim: ')), 1):
#     print('   ' + str(numero))

# --------------------------------------------------------------------------------- #

# Cria uma tabuada de multiplicação do número desejado

tabuada = int(input('Digite um número para exibir a tabuada: '))
print('Tabuada do número ', tabuada)
for valor in range(1, 11, 1):
    print(str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada*valor)))
usuarios = {}
resp = 'S'
emails = []
while resp == 'S':
    emails.append(input('Digite um e-mail: ').lower())
    resp = input('Digite <S> para continuar: ').upper()

# Criando a lista de tuplas com o índice e o e-mail
tupla = list(enumerate(emails))

# Coletando o nome e o nível para cada e-mail
for chave in range(0, len(tupla)):
    print('Email: ', tupla[chave][1])
    nome = input('Digite o nome: ')
    nivel = input('Digite o nível: ')
    usuarios[tupla[chave][1]] = [nome, nivel]  # O e-mail é a chave, e o nome e nível são os valores

# Exibindo as informações dos usuários
for chave, dado in usuarios.items():
    print('Email......: ', chave)
    print('Nome.......: ', dado[0])
    print('Nível......: ', dado[1])

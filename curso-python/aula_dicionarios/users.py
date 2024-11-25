usuarios = {}

# \n quebra linha
# + faz concatenação
opcao = input('<I> - Para Inserir um usuário \n' +
              '<P> - Para Pesquisar um usuário \n' +
              '<E> - Para Excluir um usuário \n' +
              '<L> - Para Listar um usuário \n' +
              'O que deseja realizar? ').upper()

while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        chave = input('Digite o login: ').upper()
        nome = input('Digite o nome: ').upper()
        data = input('Digite a última data de acesso: ')
        estacao = input('Qual a útima estação acessada: ').upper()
        usuarios[chave] = [nome, data, estacao]
    opcao = input('<I> - Para Inserir um usuário \n' +
              '<P> - Para Pesquisar um usuário \n' +
              '<E> - Para Excluir um usuário \n' +
              '<L> - Para Listar um usuário \n' +
              'O que deseja realizar? ').upper()
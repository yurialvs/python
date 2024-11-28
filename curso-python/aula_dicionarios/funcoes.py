# Função - Opções de navegação
# \n quebra linha
# + faz concatenação
def perguntar():
    resposta = input('<I> - Para Inserir um usuário \n' +
                '<P> - Para Pesquisar um usuário \n' +
                '<E> - Para Excluir um usuário \n' +
                '<L> - Para Listar um usuário \n' +
                'O que deseja realizar? ').upper()
    return resposta

# Função - Inserir usuário
def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
        input('Digite a última data de acesso: '),
        input('Qual a última estação acessada: ').upper()]
    
# Função - Pesquisar usuário
def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print('Nome...........: ' + lista[0])
        print('Último acesso..: ' + lista[1])
        print('Última estação.: ' + lista[2])

# Função - Excluir usuário
def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario.get[chave]
    print('Usuário excluído!')

# Função - Listar usários
def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Usuário............')
        print('Login...: ', chave)
        print('Dados...: ', valor)

# ---------------------------------------------------------------------- #

# MÉTODOS ADICIONAIS PARA DICIONÁRIOS

# items()
# Resposável por retornar em forma de lista os elementos do dicionário.

# values()
# Retorna somente os dados, descartando as chaves.

# keys()
# Retorna soementa as chaves.

# has_keys()
# Retorna se a chave existe ou não dentro do dicionário. Ture(1) ou False(0)

# clear()
# Esvazia completamente o dicionário

# popitem
# Executa de maneira aleatória, individualmente, e na sequência, deverão ser eliminados do dicionário.

# ---------------------------------------------------------------------- #

# DECISÕES SIMPLES

#nome = input('Digite o nome: ')
#idade = int(input('Digite a idade: '))
#prioridade = 'NÃO'
#if idade >= 65:
#   prioridade = 'SIM'
#print('O paciente ' + nome + ' possui atendimento prioritário? ' + prioridade)

# --------------------------------------------------------------------------------- #

# DECISÕES COMPOSTAS

#nome = input('Digite o nome: ')
#idade = int(input('Digite a idade: '))
#if idade >= 65:
#    print('O paciente ' + nome + ' possui atendimento prioritário!')
#else:
#    print('O paciente ' + nome + ' NÃO possui atendimento prioritário!')

# --------------------------------------------------------------------------------- #

# DECISÕES COMPOSTAS

#nome = input("Digite o nome: ")
#idade = int(input("Digite a idade: "))
#doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? ').upper()
## Função .upper() converte as letras para maiúscula
## Função .lower() converte as letras para minúculas
#if idade >= 65:
#    print(f'O paciente {nome}  POSSUI atendimento prioritário!')
#elif doenca_infectocontagiosa == 'SIM':
#    print(f'O paciente {nome} deve ser direcionado para sala de espera reservada.')
#else:
#    print(f'O paciente {nome} NÃO possui atendimento prioritário e pode aguardar na sala comum!')

# --------------------------------------------------------------------------------- #

# DECISÕES COMPOSTAS

# nome = input('Digite o nome: ')
# idade = int(input('Digite a idade: '))
# doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? ').upper()
# if idade >= 65 and doenca_infectocontagiosa == 'SIM':
#    print('O paciente será direcionado para sala AMARELA - COM prioridade')
# elif idade < 65 and doenca_infectocontagiosa == 'SIM':
#    print('O paciente será direcionado para sala AMARELA - SEM prioridade')
# elif idade >= 65 and doenca_infectocontagiosa == 'NÃO':
#    print('O paciente será direcionado para sala BRANCA - COM prioridade')
# elif idade < 65 and doenca_infectocontagiosa == 'NÃO':
#    print('O paciente será direcionado para sala BRANCA - SEM prioridade')
# else:
#    print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')

# --------------------------------------------------------------------------------- #

# DECISÕES ENCADEADAS

# nome = input('Digite o nome: ')
# idade = int(input('Digite a idade: '))
# doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa? ').upper()

# # Se o paciente tiver a idade maior ou igual a 65, COM prioridade
# if idade >= 65:
#     print('Paciente COM prioridade')
#     if doenca_infectocontagiosa == 'SIM':
#         print('Encaminhe o paciente para sala AMARELA')
#     elif doenca_infectocontagiosa == 'NÃO':
#         print('Encaminhe o paciente para sala BRANCA')
#     else:
#         print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')

# # Se o paciente tiver a idade menor que 65, SEM prioridade      
# else:
#     print('Paciente SEM prioridade')
#     if doenca_infectocontagiosa == 'SIM':
#         print('Encaminhe o paciente para a sala AMARELA')
#     elif doenca_infectocontagiosa == 'NÃO':
#         print('Encaminhe o paciente para a sala BRANCA')
#     else:
#         print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')

# --------------------------------------------------------------------------------- #

# DECISÕES ENCADEADAS

# nome = input('Digite o nome: ')
# idade = int(input('Digite a idade: '))
# doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa? ').upper()

# # PRIMEIRO PROBLEMA A SER RESOLVIDO
# if doenca_infectocontagiosa == 'SIM':
#     print('Encaminhe o paciente para sala AMARELA')
# elif doenca_infectocontagiosa == 'NÃO':
#     print('Encaminhe o paciente para sa sala BRANCA')
# else:
#     print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')

# # SEGUNDO PROBLEMA A SER RESOLVIDO
# if idade >= 65:
#     print('Paciente COM prioridade')
# else:
#     genero = input('Digite o gênero do paciente: ').upper()
#     if genero == 'FEMININO' and idade > 10:
#         gravidez = input('A paciente está gravida? ').upper()
#         if gravidez == 'SIM':
#             print('Paciente COM prioridade')
#         else:
#             print('Paciente SEM prioridade')
#     else:
#         print('Paciente SEM prioridade')

# --------------------------------------------------------------------------------- #

# DECISÕES ENCADEADAS

nivel = input('Digite o nível de acesso: ').upper()
if nivel == 'ADM' or nivel == 'USR':
    genero = input('Digite o seu gênero: ').upper()
    if nivel == 'ADM':
        if genero == 'FEMININO':
            print('Olá administradora')
        else:
            print('Olá administrador')
    else:
        if genero == 'FEMININO':
            print('Olá usuária')
        else:
            print('Olá usuário')
elif nivel == 'GUEST':
    print('Olá visitante')
else:
    print('Olá desconhecido(a)')
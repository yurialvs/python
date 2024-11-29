# Faz a leitura de um arquivo existente.

with open('./curso-python/aula_manipula_arquivos/teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print('Tipo de dado da variável', type(conteudo))
print('Conteúdo do arquivo: ', conteudo)
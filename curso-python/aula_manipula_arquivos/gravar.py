# Funções - Manipulação de arquivos

# open('<caminhoDoArquivo><nomeDoArquivo>', 'w')
# Abre um arquivo para modo de escrita (w => write), permite que escreva no arquivo,
# caso já exista, será sobrescrito.

# open('<caminhoDoArquivo><nomeDoArquivo>', 'r')
# Abrirá um arquivo em modo de leitura, sem possibilidade de fazer edição (r => read)

# open('<caminhoDoArquivo><nomeDoArquivo>', 'a')
# Poderá ler e escrever no arquivo especificado,
# podendo acrescentar conteúdo ao final de acordo com algum evento (a => append)

# open('<caminhoDoArquivo><nomeDoArquivo>', 'x')
# Permite criar um novo arquivo em modo exclusivo, ou seja, uma vez que você criou/abriu o arquivo,
# ninguém mais poderá abri-lo (x => eXclusive)

# open('<caminhoDoArquivo><nomeDoArquivo>', 't')
# O arquvi que for aberto com o parâmetro (t = text), irá retornar para o Python o seu conteúdo como string, 
# diferentemente do parâmetro 'b' que retornaria os dados em formato binário exigiria uma conversão para string, 
# caso fosse necessário.

# ----------------------------------------------------------------------- #
# Caminho relativo de acordo com o repositório python "./curso-python/aula...."

# Primeira operação de escrita (sobrescreve o arquivo)
with open('./curso-python/aula_manipula_arquivos/teste.txt', 'w') as arquivo:
    arquivo.write('Texto 01. \n')

# Segunda operação de escrita (adiciona ao arquivo)
with open('./curso-python/aula_manipula_arquivos/teste.txt', 'a') as arquivo:
    arquivo.write('Texto 02.')
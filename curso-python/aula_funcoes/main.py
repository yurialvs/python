# ********************************************************************************** #

# O "from" deverá receber o local físico no qual se encontram as funções que se deseja importar. 
# Já no "import", você deverá definir qual ou quais funções deseja importar.
# Se utiliza um asterisco "*", ele importará todas as funções contidas no "from".

# ********************************************************************************** #

from funcoes import *

minhaLista = []
print('Preenchendo')
preencherInventario(minhaLista)
print('Exibindo')
exibirInventario(minhaLista)

print('Pesquisando')
localizarPorNome(minhaLista)
print('Alterando')
depreciarPorNome(minhaLista, 20)

print('Excluindo')
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print('Resumindo')
resumirValores(minhaLista)

# --------------------------------------------------------------------------------- #


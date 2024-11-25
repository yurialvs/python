usuarios = {}

# Fulano e Ciclano são duas chaves que são separadas por um virgula, após os dois pontos (:) surgem os dados das chaves
# Caso o objeto que estiver na segunda linha irá sobrescrever o objeto que estava na primeira linha.
usuarios = {'Fulano': ['Fulano Silva', '17/06/2017', 'Recep_01'],
            'Ciclano': ['Ciclano Santos', '03/06/2017', 'Raiox_02'],
            'Ciclano': ['Ciclano Santos', '03/06/2017', 'Raiox_10']
            }

# Adicionando itens no dicionário:
usuarios['Beltrano'] = ['Beltrano Santos', '26/11/2017', 'Recep_01']
usuarios['Beltrano'] = ['Beltrano Santos', '10/01/2010', 'Recep_01']

# De acordo com o código acima, ao executar o Python irá armazenar dentro do dicionário "usuarios" apenas três objetos, 
# um com a chave "Fulano", outro com a chave "Ciclano", outro com chave ""


# Implementação da Lista Encadeada
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

# Implementação da Tabela Hash com Listas Encadeadas
class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        char1, char2 = sigla
        posicao = (ord(char1) + ord(char2)) % 10
        return posicao

    def inserir(self, sigla, nomeEstado):
        indice = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        novo_nodo.proximo = self.tabela[indice]
        self.tabela[indice] = novo_nodo

    def imprimir_tabela(self):
        for i, nodo in enumerate(self.tabela):
            print(f"Posição {i}:", end=" ")
            atual = nodo
            while atual is not None:
                print(atual.sigla, end=" -> ")
                atual = atual.proximo
            print("None")

# Inicialização da Tabela Hash
tabela = TabelaHash()

# Impressão inicial da Tabela Hash (vazia)
print("Tabela Hash inicial:")
tabela.imprimir_tabela()

# Inserção dos 26 estados e Distrito Federal
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), 
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), 
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), 
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), 
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), 
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), 
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

for sigla, nome in estados:
    tabela.inserir(sigla, nome)

# Impressão da Tabela Hash após inserir estados e Distrito Federal
print("\nTabela Hash após inserir estados e DF:")
tabela.imprimir_tabela()

# Inserção do estado fictício
estado_ficticio_sigla = "YL"
estado_ficticio_nome = "Yuri Alves Lopes"
tabela.inserir(estado_ficticio_sigla, estado_ficticio_nome)

# Impressão da Tabela Hash após inserir estado fictício
print("\nTabela Hash após inserir estado fictício:")
tabela.imprimir_tabela()

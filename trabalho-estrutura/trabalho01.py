class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEspera:
    def __init__(self):
        self.head = None
    
    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo
    
    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A' and atual.proximo.numero < nodo.numero:
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo
    
    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        numero = int(input("Digite o número do cartão: "))
        nodo = Nodo(numero, cor)
        
        if self.head is None:
            self.head = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        elif cor == 'A':
            self.inserirComPrioridade(nodo)
    
    def imprimirListaEspera(self):
        atual = self.head
        while atual:
            print(f"Cartão {atual.cor} - Número {atual.numero}")
            atual = atual.proximo
    
    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            paciente = self.head
            self.head = self.head.proximo
            print(f"Chamando paciente com cartão {paciente.cor} - Número {paciente.numero} para atendimento.")
    
    def menu(self):
        while True:
            print("\nMenu:")
            print("1 - Adicionar paciente à fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar próximo paciente")
            print("4 - Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimirListaEspera()
            elif opcao == '3':
                self.atenderPaciente()
            elif opcao == '4':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

# Execução do programa
lista_espera = ListaEspera()
lista_espera.menu()
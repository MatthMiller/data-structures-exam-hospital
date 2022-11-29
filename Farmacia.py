from ListaEncadeada import *
import os

class Farmacia:
    def __init__(self):
        # Aqui a lista encadeada é preenchida pelos dados existentes
        # do json. Depois se atualiza a cada adição ou deleção
        self.listaMedicamentos = ListaEncadeada()

        self.clearConsole()

        self.listaMedicamentos.insere_no_inicio({'nome': 'Amoxilina', 'quantidade': '2'})
        self.listaMedicamentos.insere_no_inicio({'nome': 'Neosaldina', 'quantidade': '5'})
        self.listaMedicamentos.insere_no_inicio({'nome': 'Soro antiofídico', 'quantidade': '10'})
        self.listaMedicamentos.insere_no_inicio({'nome': 'Penicilina', 'quantidade': '1'})

        self.statusFarmacia()

    def exibirMedicamentos(self):
        print('\n📦 Lista de medicamentos em estoque:')
        if (self.listaMedicamentos.cabeca == None):
            print('< Sem medicamentos no estoque! >')
        else: 
            self.listaMedicamentos.exibir_medicamentos()
        
        self.esperarPressionarEnter()

    def buscarMedicamento(self, nome):
        print('\n🔍 Itens encontrados:')

        if(self.listaMedicamentos.busca_medicamento(nome)):
            print(self.listaMedicamentos.busca_medicamento(nome))
        else:
            print('< Nenhum item encontrado! >')

        self.esperarPressionarEnter()

    def inserirMedicamento(self, nome, quantidade):
        self.listaMedicamentos.insere_no_inicio({'nome': nome, 'quantidade': quantidade})
        print('\nMedicamento ' + nome + ' inserido com sucesso!')
        # atualizar no json tb
        self.esperarPressionarEnter()

    def excluirMedicamento(self, nome):
        self.listaMedicamentos.excluir_medicamento(nome)
        self.esperarPressionarEnter()

    def esperarPressionarEnter(self):
        input('\nPressione enter para escolher outra opção...')
        self.statusFarmacia()

    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def statusFarmacia(self):
        self.clearConsole()
        print('💉 Bem-vindo à farmácia hospitalar FacensCare \n\n')

        print('Opções disponíveis: \n')
        print('(1) Exibir lista de medicamentos')
        print('(2) Buscar medicamento')
        print('(3) Inserir novo medicamento')
        print('(4) Deletar medicamento')
        print('(5) Voltar para a tela de atendimentos')

        opcaoEscolhida = input('Digite a opção: ')
        if (opcaoEscolhida == '1'):
            self.exibirMedicamentos()
        elif (opcaoEscolhida == '2'):
            medicamentoBuscado = input('\nDigite o nome do medicamento a ser buscado: ')
            self.buscarMedicamento(medicamentoBuscado)
        elif (opcaoEscolhida == '3'):
            medicamentoEscolhido = input('\nDigite o nome do medicamento a ser inserido: ')
            quantidadeEscolhida = input('Digite quantidade desse medicamento: ')
            self.inserirMedicamento(medicamentoEscolhido, quantidadeEscolhida)
        elif (opcaoEscolhida == '4'):
            medicamentoBuscado = input('\nDigite o nome de um medicamento a ser deletado: ')
            self.excluirMedicamento(medicamentoBuscado)
        elif (opcaoEscolhida == '5'):
            pass
        else:
            self.statusFarmacia()
        
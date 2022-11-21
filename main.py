import os
import copy
from Queue import *

class Hospital:
    def __init__(self):
        self.filaEmergencia = Queue()
        self.filaComum = Queue()

        self.statusFila()

    def mostrarPacientes(self, tipo):
        if (tipo == 'comum'):
            fila = copy.deepcopy(self.filaComum)
        elif (tipo == 'emergencial'):
            fila = copy.deepcopy(self.filaEmergencia)

        if (not fila.isEmpty()):
            filaStatus = ''
            for x in range(fila.size()):
                filaStatus += str(fila.dequeue()) + ' '
        else:
            filaStatus = '< Fila vazia! >\n'
        
        print(str(filaStatus) + '\n')

    def adicionarPaciente(self, nome, tipoPaciente):
        if (tipoPaciente.lower() == 'c'):
            self.filaComum.enqueue(nome)
        elif(tipoPaciente.lower() == 'e'):
            self.filaEmergencia.enqueue(nome)
        self.statusFila()

    def andarAtendimento(self, resposta):
        if (resposta.lower() == 's'):
            if (not self.filaEmergencia.isEmpty()):
                self.filaEmergencia.dequeue()
            elif (not self.filaComum.isEmpty()):
                self.filaComum.dequeue()                
            self.statusFila()
        elif (resposta.lower() == 'n'):
            pass

    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def statusFila(self):
        self.clearConsole()
        print('🏥 Bem-vindo ao hospital FacensCare \n\n')
        print('Fila emergencial de pacientes:')
        self.mostrarPacientes('emergencial')
        print('Fila comum de pacientes:')
        self.mostrarPacientes('comum')

        andarAtendimento = input('Deseja fazer andar o atendimento? (s/n): ')
        self.andarAtendimento(andarAtendimento)
        nomePaciente = input('Digite o nome do novo paciente a ser inserido: ')
        tipoPaciente = input('Fila comum ou emergencial? (c/e): ')
        self.adicionarPaciente(nomePaciente, tipoPaciente)

Hospital()
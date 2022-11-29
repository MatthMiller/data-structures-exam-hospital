class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(lista, novo_dado):
        # 1) Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NodoLista(novo_dado)

        # 2) Faz com que o novo nodo seja a cabeça da lista.
        novo_nodo.proximo = lista.cabeca

        # 3) Faz com que a cabeça da lista referencie o novo nodo.
        lista.cabeca = novo_nodo
    
    def insere_depois(lista, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista."

        # Cria um novo nodo com o dado desejado.
        novo_nodo = NodoLista(novo_dado)

        # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_nodo.proximo = nodo_anterior.proximo

        # Faz com que o novo nodo seja o próximo do nodo anterior.
        nodo_anterior.proximo = novo_nodo

    def busca_medicamento(lista, valor):
        corrente = lista.cabeca
        listaConcatenada = ''
        contador = 0

        while corrente and corrente.dado != valor:
            if (valor.lower() in corrente.dado['nome'].lower()):
                if (contador > 0):
                    listaConcatenada += '\n' + str(corrente.dado['nome']) + ' (x' + str(corrente.dado['quantidade']) + ')'
                else:
                    listaConcatenada += str(corrente.dado['nome']) + ' (x' + str(corrente.dado['quantidade']) + ')'
                contador += 1
            corrente = corrente.proximo
        # return corrente
        if(listaConcatenada != ''):
            return listaConcatenada
        else:
            return False

    def somar_impares(lista):
        corrente = lista.cabeca
        valoresImpares = 0
        if (corrente != None): 
            if (corrente.dado % 2 != 0):
                valoresImpares += corrente.dado
        while corrente and corrente.dado != None:
            corrente = corrente.proximo
            if (corrente != None):
                if (corrente.dado % 2 != 0):
                    valoresImpares += corrente.dado
        return valoresImpares

    def verifica_igual_array(lista, arrayArg):
        corrente = lista.cabeca
        somaIgualdades = 0

        if (corrente != None): 
            if (corrente.dado == arrayArg[0]):
                somaIgualdades += 1
                # print(str(corrente.dado) + ' ' + str(arrayArg[0]))
        indice = 1
        while corrente and corrente.dado != None:
            corrente = corrente.proximo
            if (corrente != None):
                if (corrente.dado == arrayArg[indice]):
                    somaIgualdades += 1
                    # print(str(corrente.dado) + ' ' + str(arrayArg[indice]))                    
            indice += 1
        
        if (somaIgualdades == len(arrayArg)):
            return True
        else:
            return False
    
    def excluir_medicamento(self, valor):
        assert self.cabeca, "Impossível remover valor de lista vazia."

        # Nodo a ser removido é a cabeça da lista.
        if self.cabeca.dado['nome'] == valor:
            self.cabeca = self.cabeca.proximo
            # print('❌ ' + self.cabeca.dado['nome'] + '(x' + self.cabeca.dado['quantidade'] + ')' + ' removido!')
        else:
            # Encontra a posição do elemento a ser removido.
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado['nome'] != valor:
                anterior = corrente
                corrente = corrente.proximo
                # print('❌ ' + corrente.dado['nome'] + '(x' + corrente.dado['quantidade'] + ')' + ' removido!')
            # O nodo corrente é o nodo a ser removido.
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                # O nodo corrente é a cauda da lista.
                anterior.proximo = None

    def remove_em_intervalo(lista, a, b):
        corrente = lista.cabeca
        if (corrente != None): 
            if (corrente.dado >= a and corrente.dado <= b):
                lista.remove(corrente.dado)
        while corrente and corrente.dado != None:
            corrente = corrente.proximo
            if (corrente != None): 
                if (corrente.dado >= a and corrente.dado <= b):
                    lista.remove(corrente.dado)
    
    def exibir_medicamentos(lista):
        corrente = lista.cabeca
        listaConcatenada = ''

        if (corrente != None): 
            # print('corrente.dado: ' + str(corrente.dado)) # primeiro elemento
            # print('lista.cabeca: ' + str(lista.cabeca)) # a própria lista
            listaConcatenada += str(corrente.dado['nome']) + ' (x' + str(corrente.dado['quantidade']) + ')'
        
        while corrente and corrente.dado != None:
            corrente = corrente.proximo
            if (corrente != None):
                # print('corrente.dado: ' + str(corrente.dado))
                listaConcatenada += '\n' + str(corrente.dado['nome']) + ' (x' + str(corrente.dado['quantidade']) + ')'
        
        print(listaConcatenada)

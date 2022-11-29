from ListaEncadeada import *

lista = ListaEncadeada()

array = [32, 12, 66, 3, 5]

lista.insere_no_inicio(5)
lista.insere_no_inicio(3)
lista.insere_no_inicio(66)
lista.insere_no_inicio(12)
lista.insere_no_inicio(32)
print(lista)
print(array)

if (lista.verifica_igual_array(array)):
    print('As listas são iguais!')
else: 
    print('As listas são diferentes!')
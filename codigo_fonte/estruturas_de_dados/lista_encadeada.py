""" Exemplo de estrutura de lista encadeada simples e alguns algoritmos relacionados.
Essa estrutura se trata de uma sequência de nodos ligados, ou encadeadas, uns aos outros por uma referência.
Os nodos de uma lista encadeada são compostas de dois elementos cada. O primeiro elemento é o dado
efetivo a ser armazenado e o segundo se trata de uma referência para o próximo elemento da lista. A lista
encadeada simples só poderá ser transcorrida em um sentido, do início ao fim.
A principal vantagem da utilização de listas encadeadas sobre listas sequenciais é o ganho em desempenho em
termos de velocidade nas inclusões e remoções de elementos. Entretanto para acessar um item da lista é
necessário transcorrê-la em partes, ou no pior caso ,inteira.
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "14/08/2022"
__credits__ = ["https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm",
               "https://towardsdatascience.com/python-linked-lists-c3622205da81",
               "https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/"]
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"


from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa um único nó de uma lista """

    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    """
    Representa uma lista cujos elementos (nós) estão encadeados por elos.
    A lista encadeada simples só pode ser iterada em um único sentido (para frente).
    """

    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    @property
    def valores(self):
        """ Conjunto dos nós. """
        return [nodo.valor for nodo in self]

    def adicionar_inicio(self, valor):
        """ Adiciona um novo nó no início da lista. """
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        self._tamanho += 1

    def adicionar_final(self, valor):
        """ Adiciona um novo nó ao final da lista. """
        novo_nodo = Nodo(valor)
        if self.cabeca is None:
            self.cabeca = novo_nodo
            self._tamanho += 1
            return
        ultimo = self.cabeca
        while ultimo.proximo:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_nodo
        self._tamanho += 1

    def adicionar_pos(self, pos_nodo, valor):
        """ Adiciona um novo nó em uma posição posterior à outro nó específico. """
        nodo_temp = self.buscar(pos_nodo)
        if nodo_temp is None:
            print(FAIL + "ATENÇÃO!" + ENDC + " Nó '" + pos_nodo + "' não foi encontrado! Inserção não ocorreu.")
            return
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = nodo_temp.proximo
        nodo_temp.proximo = novo_nodo
        self._tamanho += 1

    def remover(self, valor):
        """ Remove um nó específico. """
        nodo_temp = self.cabeca
        nodo_anterior = None
        # Se o nó a ser excluído for a cabeça da lista
        if nodo_temp is not None and nodo_temp.valor == valor:
            self.cabeca = nodo_temp.proximo
            self._tamanho -= 1
            return
        else:
            while nodo_temp is not None and nodo_temp.valor != valor:
                nodo_anterior = nodo_temp
                nodo_temp = nodo_temp.proximo
            if nodo_temp is None:
                print(FAIL + "ATENÇÃO!" + ENDC + " Nó '" + str(valor) + "' não foi encontrado! Exclusão não ocorreu.")
                return
            nodo_anterior.proximo = nodo_temp.proximo
            self._tamanho -= 1

    def buscar(self, valor):
        """ Busca um nó especificado. """
        for nodo in self:
            if nodo.valor == valor:
                return nodo
        return None

    def esta_vazia(self):
        if self._tamanho <= 0:
            return True
        return False

    def __iter__(self):
        nodo_atual = self.cabeca
        while nodo_atual:
            yield nodo_atual
            nodo_atual = nodo_atual.proximo

    def __len__(self):
        return self._tamanho

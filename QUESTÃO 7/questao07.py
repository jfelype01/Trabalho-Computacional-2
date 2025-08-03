# Equipe 2:
# Antonio Misson Junqueira
# Artur Fernandes Braga
# Davi de Menezes Belchior
# Fabrício Alves Ribeiro
# João Felype Morais Vieira
# João Victor de Sousa Ribeiro

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo_no = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca_lista = None

    def inserir_valor(self, valor):
        novo_no = No(valor)
        if not self.cabeca_lista:
            self.cabeca_lista = novo_no
        else:
            no_atual = self.cabeca_lista
            while no_atual.proximo_no:
                no_atual = no_atual.proximo_no
            no_atual.proximo_no = novo_no

    def tamanho_lista(self):
        no_atual = self.cabeca_lista
        count = 0
        while no_atual:
            count += 1
            no_atual = no_atual.proximo_no
        return count
    
    def get_no(self, indice_no):
        if indice_no < 0:
            return None
        
        no_atual = self.cabeca_lista
        for _ in range(indice_no):
            if no_atual:
                no_atual = no_atual.proximo_no
            else:
                return None
            
        return no_atual

    def busca_sequencial(self, valor_alvo):
        no_atual = self.cabeca_lista
        pos = 0
        while no_atual:
            if no_atual.valor == valor_alvo:
                return pos
            no_atual = no_atual.proximo_no
            pos += 1
        return -1
    
    def _inserir_ordenado(self, inicio, novo_no):
        if not inicio or novo_no.valor < inicio.valor:
            novo_no.proximo_no = inicio
            return novo_no
        
        atual = inicio

        while atual.proximo_no and atual.proximo_no.valor < novo_no.valor:
            atual = atual.proximo_no
        
        novo_no.proximo_no = atual.proximo_no
        atual.proximo_no = novo_no
        return inicio
    
    def ordenar_lista_insertion_sort(self):
        if not self.cabeca_lista or not self.cabeca_lista.proximo_no:
            return
        
        lista_ordenada = None

        no_atual = self.cabeca_lista
        
        while no_atual:
            proximo = no_atual.proximo_no
            no_atual.proximo_no = None
            lista_ordenada = self._inserir_ordenado(lista_ordenada, no_atual)
            no_atual = proximo

        self.cabeca_lista = lista_ordenada

    def busca_binaria(self, valor_alvo):
        inicio = 0
        fim = self.tamanho_lista() - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            no_do_meio = self.get_no(meio)
            if not no_do_meio:
                return -1
            if no_do_meio.valor == valor_alvo:
                return meio
            elif no_do_meio.valor < valor_alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

import random

def main():
    lista = ListaEncadeada()
    numeros = random.sample(range(1, 100), 10)

    for num in numeros:
        lista.inserir_valor(num)

    valor_alvo = random.choice(numeros)
    print(f"Buscando o número {valor_alvo}...\n")

    print("Lista encadeada desordenada:", numeros)

    posicao_sequencial = lista.busca_sequencial(valor_alvo)

    lista.ordenar_lista_insertion_sort()

    valores_ordenados = []
    no_atual = lista.cabeca_lista
    while no_atual:
        valores_ordenados.append(no_atual.valor)
        no_atual = no_atual.proximo_no

    print("\nLista encadeada ordenada:", valores_ordenados)


    print("\nPosição do valor na lista (Busca Sequencial): ", posicao_sequencial + 1)

    posicao_binaria = lista.busca_binaria(valor_alvo)
    print("Posição do valor na lista (Busca Binária): ", posicao_binaria + 1)

if __name__ == "__main__":
    main()
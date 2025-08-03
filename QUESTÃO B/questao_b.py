# Equipe 2:
# Antonio Misson Junqueira
# Artur Fernandes Braga
# Davi de Menezes Belchior
# Fabrício Alves Ribeiro
# João Felype Morais Vieira
# João Victor de Sousa Ribeiro

import random
import time
import matplotlib.pyplot as plt

#Funções de busca
def busca_linear(vetor, chave):
    for i, valor in enumerate(vetor):
        if valor == chave:
            return i
    return -1

def busca_linear_sentinela(vetor, chave):
    vetor.append(chave)
    i = 0
    while vetor[i] != chave:
        i += 1
    vetor.pop()
    return i if i < len(vetor) else -1

def busca_binaria(vetor, chave):
    inicio, fim = 0, len(vetor) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] == chave:
            return meio
        elif vetor[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

def busca_binaria_rapida(vetor, chave):
    def helper(inicio, fim):
        if inicio > fim:
            return -1
        meio = (inicio + fim) // 2
        if vetor[meio] == chave:
            return meio
        elif vetor[meio] < chave:
            return helper(meio + 1, fim)
        else:
            return helper(inicio, meio - 1)
    return helper(0, len(vetor) - 1)

#Método de ordenação linear
def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

#Testes
tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
tempos_linear = []
tempos_linear_sentinela = []
tempos_binaria = []
tempos_binaria_rapida = []

for tamanho in tamanhos:
    vetor = [random.randint(0, 1000000) for _ in range(tamanho)]
    chave = random.choice(vetor)

    #Busca linear
    inicio = time.time()
    busca_linear(vetor, chave)
    tempos_linear.append(time.time() - inicio)

    #Busca linear com sentinela
    inicio = time.time()
    busca_linear_sentinela(vetor[:], chave)
    tempos_linear_sentinela.append(time.time() - inicio)

    #Ordena o vetor para buscas binárias
    vetor_ordenado = vetor[:]
    insertion_sort(vetor_ordenado)

    #Busca binária
    inicio = time.time()
    busca_binaria(vetor_ordenado, chave)
    tempos_binaria.append(time.time() - inicio)

    #Busca binária rápida
    inicio = time.time()
    busca_binaria_rapida(vetor_ordenado, chave)
    tempos_binaria_rapida.append(time.time() - inicio)

#Gráficos 
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_linear, label='Busca Linear', marker='o')
plt.plot(tamanhos, tempos_linear_sentinela, label='Busca Linear Sentinela', marker='o')
plt.plot(tamanhos, tempos_binaria, label='Busca Binária', marker='o')
plt.plot(tamanhos, tempos_binaria_rapida, label='Busca Binária Rápida', marker='o')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo de execução (s)')
plt.title('Comparação de Tempo das Buscas')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
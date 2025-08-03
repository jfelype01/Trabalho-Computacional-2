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

# --- 1) Implementação dos 10 algoritmos ---

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita  = lista[meio:]
        merge_sort(esquerda)
        merge_sort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]; i += 1
            else:
                lista[k] = direita[j]; j += 1
            k += 1
        while i < len(esquerda):
            lista[k] = esquerda[i]; i += 1; k += 1
        while j < len(direita):
            lista[k] = direita[j]; j += 1; k += 1

def quick_sort(lista):
    def _qs(arr, ini, fim):
        if ini < fim:
            p = particionar(arr, ini, fim)
            _qs(arr, ini, p - 1)
            _qs(arr, p + 1, fim)
    def particionar(arr, ini, fim):
        pivot = arr[fim]
        i = ini - 1
        for j in range(ini, fim):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
        return i + 1
    _qs(lista, 0, len(lista) - 1)

def counting_sort(lista):
    if not lista: return
    minimo = min(lista); maximo = max(lista)
    contagem = [0] * (maximo - minimo + 1)
    for x in lista:
        contagem[x - minimo] += 1
    idx = 0
    for valor, freq in enumerate(contagem):
        while freq:
            lista[idx] = valor + minimo
            idx += 1
            freq -= 1

def radix_sort(lista):
    if not lista: return
    def por_digito(arr, exp):
        n = len(arr)
        saida = [0] * n
        cont = [0] * 10
        for num in arr:
            cont[(num // exp) % 10] += 1
        for i in range(1, 10):
            cont[i] += cont[i-1]
        for i in range(n-1, -1, -1):
            d = (arr[i] // exp) % 10
            saida[cont[d] - 1] = arr[i]
            cont[d] -= 1
        for i in range(n):
            arr[i] = saida[i]
    maior = max(lista)
    exp = 1
    while maior // exp > 0:
        por_digito(lista, exp)
        exp *= 10

def bucket_sort(lista):
    if not lista: return
    minimo, maximo = min(lista), max(lista)
    num_baldes = len(lista)//10 or 1
    baldes = [[] for _ in range(num_baldes)]
    for x in lista:
        idx = (x - minimo) * (num_baldes - 1) // (maximo - minimo + 1)
        baldes[idx].append(x)
    lista.clear()
    for b in baldes:
        insertion_sort(b)
        lista.extend(b)

def shell_sort(lista):
    n = len(lista)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j-intervalo] > temp:
                lista[j] = lista[j-intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo //= 2

def heapify(lista, tamanho, raiz):
    maior = raiz
    esq = 2 * raiz + 1
    dir = 2 * raiz + 2
    if esq < tamanho and lista[esq] > lista[maior]:
        maior = esq
    if dir < tamanho and lista[dir] > lista[maior]:
        maior = dir
    if maior != raiz:
        lista[raiz], lista[maior] = lista[maior], lista[raiz]
        heapify(lista, tamanho, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range((n // 2) - 1, -1, -1):
        heapify(lista, n, i)
    for fim in range(n - 1, 0, -1):
        lista[0], lista[fim] = lista[fim], lista[0]
        heapify(lista, fim, 0)

# --- 2) Dicionário de algoritmos ---

algoritmos = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Counting Sort": counting_sort,
    "Radix Sort": radix_sort,
    "Bucket Sort": bucket_sort,
    "Shell Sort": shell_sort,
    "Heap Sort": heap_sort
}

# --- 3) Coleta de tempos de execução ---

tamanhos_vetor = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
tempos_execucao = {nome: [] for nome in algoritmos}

for n in tamanhos_vetor:
    lista_original = [random.randint(1, n) for _ in range(n)]
    for nome, func in algoritmos.items():
        copia = lista_original.copy()
        inicio = time.perf_counter()
        func(copia)
        fim = time.perf_counter()
        tempos_execucao[nome].append(fim - inicio)
    print(f"Tamanho {n} concluído")

# --- 4) Gráfico geral (Figura 1) ---

plt.figure(figsize=(10, 6))
for nome, t in tempos_execucao.items():
    plt.plot(tamanhos_vetor, t, label=nome)
plt.title("Figura 1 – Desempenho Geral dos Algoritmos")
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo (segundos)")
plt.legend(bbox_to_anchor=(1,1))
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 5) Gráficos específicos (Figura 2) ---

# 2a) Quadráticos
plt.figure(figsize=(8, 4))
for nome in ["Bubble Sort", "Insertion Sort", "Selection Sort"]:
    plt.plot(tamanhos_vetor, tempos_execucao[nome], label=nome)
plt.title("Figura 2a – Algoritmos Quadráticos (O(n²))")
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2b) Eficientes
plt.figure(figsize=(8, 4))
for nome in ["Merge Sort", "Quick Sort", "Heap Sort"]:
    plt.plot(tamanhos_vetor, tempos_execucao[nome], label=nome)
plt.title("Figura 2b – Algoritmos Eficientes (O(n log n))")
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
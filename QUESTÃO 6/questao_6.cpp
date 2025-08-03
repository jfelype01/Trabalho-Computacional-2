// Equipe 2:
// Antonio Misson Junqueira
// Artur Fernandes Braga
// Davi de Menezes Belchior
// Fabrício Alves Ribeiro
// João Felype Morais Vieira
// João Victor de Sousa Ribeiro

#include <iostream>

//Struct do nó da lista duplamente encadeada
struct Node {
    int data;
    Node* prev;
    Node* next;

    //Construtor do nó
    Node(int val) : data(val), prev(nullptr), next(nullptr) {}
};


//Classe da lista duplamente encadeada
class LinkedList {
public:
    Node* head;
    Node* tail;

	//Construtor da lista
    LinkedList() : head(nullptr), tail(nullptr) {}

	//Função para adicionar um nó no final da lista
    void push_back(int val) {
        Node* node = new Node(val);
        if (!head) {
            head = tail = node;
        }
        else {
            tail->next = node;
            node->prev = tail;
            tail = node;
        }
    }

	//Função para imprimir a lista
    void print() const {
        Node* cur = head;
        while (cur) {
            std::cout << cur->data << " ";
            cur = cur->next;
        }
        std::cout << "\n";
    }

    //Destrutor da lista
    ~LinkedList() {
        Node* cur = head;
        while (cur) {
            Node* tmp = cur;
            cur = cur->next;
            delete tmp;
        }
    }
};


//Função que realiza a ordenação por Insertion Sort
void insertionSort(LinkedList& list) {
    if (!list.head || !list.head->next) return;

    Node* it = list.head->next;

    while (it) {
        int current = it->data;
        Node* insertPos = it;

        Node* prev = it->prev;

        while (insertPos != list.head && prev->data > current) {
            insertPos->data = prev->data;
            insertPos = prev;
            prev = prev->prev;
        }

        insertPos->data = current;
        it = it->next;
    }
}

int main() {
    LinkedList lst;

    //Adição dos elementos teste na lista
    lst.push_back(6);
    lst.push_back(7);
    lst.push_back(5);
    lst.push_back(3);
    lst.push_back(4);
    lst.push_back(1);
    lst.push_back(2);

    std::cout << "Lista original: ";
    lst.print();

    insertionSort(lst);

    std::cout << "Lista ordenada (InsertionSort): ";
    lst.print();

    return 0;
}

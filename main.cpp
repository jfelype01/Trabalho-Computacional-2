#include <iostream>

struct Node {
    int data;
    Node* prev;
    Node* next;
    Node(int val) : data(val), prev(nullptr), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;
    Node* tail;

    LinkedList() : head(nullptr), tail(nullptr) {}

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

    void print() const {
        Node* cur = head;
        while (cur) {
            std::cout << cur->data << " ";
            cur = cur->next;
        }
        std::cout << "\n";
    }

    ~LinkedList() {
        Node* cur = head;
        while (cur) {
            Node* tmp = cur;
            cur = cur->next;
            delete tmp;
        }
    }
};

// Algoritmo insertion sort na lista manual
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

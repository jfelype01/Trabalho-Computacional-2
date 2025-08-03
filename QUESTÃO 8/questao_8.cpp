// Equipe 2:
// Antonio Misson Junqueira
// Artur Fernandes Braga
// Davi de Menezes Belchior
// Fabrício Alves Ribeiro
// João Felype Morais Vieira
// João Victor de Sousa Ribeiro

#include <iostream>
#include <vector>
#include <string>
using namespace std;

template <typename T> 
class No {
private:
    T valor;
    No<T> * pai;
    vector<No<T> *> filhos;
public:
    No(T valor, No<T> * pai = nullptr){
        this -> valor = valor;
        this -> pai = pai;
    }

    void setPai(No<T>* novoPai){
        pai = novoPai;
    }

    No<T> * getPai (){
        return pai;
    }

    T getValor(){
        return valor;
    }

    void adicionarFilho (No<T>* filho){
        filhos.push_back(filho);
    }

    vector<No<T>*> getFilhos(){
        return filhos;
    }
};

template <typename T>
class Arvore{
private:
    No<T>* raiz;

public:
    Arvore() {
        raiz = nullptr;
    }

    Arvore(T valor) {
        raiz = new No<T>(valor);
    }

    No<T>* getRaiz() {
        return raiz;
    }

   
    bool inserir(T valor, T valorPai) {
        if (!raiz) {
            raiz = new No<T>(valor);
            return true;
        }
        No<T>* pai = pesquisar(valorPai, raiz);
        if (pai) {
            No<T>* novoNo = new No<T>(valor, pai);
            pai->adicionarFilho(novoNo);
            return true;
        }
        return false;
    }

      No<T>* pesquisar(T valor, No<T>* noAtual) {
        if (!noAtual) return nullptr;
        if (noAtual->getValor() == valor) return noAtual;

        for (auto filho : noAtual->getFilhos()) {
            No<T>* resultado = pesquisar(valor, filho);
            if (resultado) return resultado;
        }
        return nullptr;
    }

    
    void exibir(No<T>* noAtual, int nivel = 0) {
        if (!noAtual) return;
        for (int i = 0; i < nivel; i++) cout << "  ";
        cout << noAtual->getValor() << endl;
        for (auto filho : noAtual->getFilhos()) {
            exibir(filho, nivel + 1);
        }
    }
};
int main() {
      Arvore<char> arvore('A');

    // Construindo a árvore do exemplo
    arvore.inserir('B', 'A');
    arvore.inserir('C', 'A');
    arvore.inserir('D', 'A');
    arvore.inserir('E', 'B');
    arvore.inserir('I', 'E');
    arvore.inserir('F', 'C');
    arvore.inserir('G', 'C');
    arvore.inserir('J', 'G');
    arvore.inserir('K', 'G');
    arvore.inserir('L', 'G');
    arvore.inserir('H', 'D');
    arvore.inserir('M', 'H');
    arvore.inserir('N', 'M');

    // Exibindo árvore
    cout << "Arvore generica:\n";
    arvore.exibir(arvore.getRaiz());

    return 0;
}
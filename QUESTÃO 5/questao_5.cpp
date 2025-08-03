// Equipe 2:
// Antonio Misson Junqueira
// Artur Fernandes Braga
// Davi de Menezes Belchior
// Fabrício Alves Ribeiro
// João Felype Morais Vieira
// João Victor de Sousa Ribeiro

#include <iostream>
#include <string>
using namespace std;

class Funcionario {
private:
    string nome;
    double salario;

public:
    // Construtor
    Funcionario() {}

    // Getters
    string getNome() const { return nome; }
    double getSalario() const { return salario; }

    // Setters
    void setNome(const string& n) { nome = n; }
    void setSalario(double s) { salario = s; }
};

// Ordena por salário usando Bubble Sort
void ordenarPorSalario(Funcionario lista[]) {
    for (int i = 0; i < 5 - 1; i++) {
        for (int j = 0; j < 5 - 1 - i; j++) {
            if (lista[j].getSalario() > lista[j + 1].getSalario()) {
                swap(lista[j], lista[j + 1]);
            }
        }
    }
}

// Ordena por nome usando Selection Sort
void ordenarPorNome(Funcionario lista[]) {
    for (int i = 0; i < 5 - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < 5; j++) {
            if (lista[j].getNome() < lista[min_idx].getNome()) {
                min_idx = j;
            }
        }
        swap(lista[i], lista[min_idx]);
    }
}

// Imprime os dados dos funcionários
void imprimirLista(Funcionario lista[]) {
    for (int i = 0; i < 5; i++) {
        cout << lista[i].getNome() << " - R$ " << lista[i].getSalario() << endl;
    }
}

int main() {
    Funcionario lista[5];

    cout << "Cadastro de 5 funcionários:\n";
    for (int i = 0; i < 5; i++) {
        string nome;
        double salario;

        cout << "Digite o nome: ";
        getline(cin >> ws, nome); 

        cout << "Salário: ";
        cin >> salario;

        lista[i].setNome(nome);
        lista[i].setSalario(salario);
    }

    Funcionario copia1[5], copia2[5];
    for (int i = 0; i < 5; i++) {
        copia1[i] = lista[i]; // para ordenar por salário
        copia2[i] = lista[i]; // para ordenar por nome
    }

    // Ordenação por salário
    ordenarPorSalario(copia1);
    cout << "\nFuncionários ordenados por salário (crescente):\n";
    imprimirLista(copia1);

    // Ordenação por nome
    ordenarPorNome(copia2);
    cout << "\nFuncionários ordenados por nome (ordem alfabética):\n";
    imprimirLista(copia2);

    return 0;
}
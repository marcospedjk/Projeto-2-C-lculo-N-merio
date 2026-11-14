# Método direto de Gauss

import numpy as np
print("""
Você deseja executar o problema proposto ou algum fornecido por você:
[1] Problema proposto
[2] Fornecer sistema""")


def metodoGauss(opcaoEscolhida):
    i = 0
    if opcaoEscolhida == 1:
        tamanhoSistema = 3
        matriz_aumentada = np.array([
            [15, 17, 19, 3890],
            [0.3, 0.4, 0.55, 95],
            [1, 1.2, 1.5, 282]
        ], dtype=float)

    else:
        while True:
            tamanhoSistema = int(input("Qual o tamanho do sistema que você quer resolver: "))
            if(tamanhoSistema < 1):
                print("Isso é um sistema impossível, o tamanho de um sistema tem que ser um valor positivo")
            else:
                break
        matriz_aumentada = np.zeros((tamanhoSistema, tamanhoSistema+1))
        while(i < tamanhoSistema):
            j = 0
            aux = 1
            print(f"Insira a equação {i+1}:")
            while(j < tamanhoSistema+1):
                if(j == tamanhoSistema):
                    matriz_aumentada[i][j] = float(input(f"b{i+1}: "))
                else:
                    matriz_aumentada[i][j] = float(input(f"x{aux}: "))
                j+=1
                aux+=1
            i+=1

    imprimirMatriz(matriz_aumentada, "Matriz aumentada")
    matriz_pos_pivoteamento = pivoteamento(matriz_aumentada, tamanhoSistema)
    imprimirMatriz(matriz_pos_pivoteamento, "Matriz pós pivoteamento")
    matriz_pos_escalonamento = escalonamento(matriz_pos_pivoteamento, tamanhoSistema)
    imprimirMatriz(matriz_pos_escalonamento, "Matriz escalonada")

    resultados = regressao(matriz_pos_escalonamento, tamanhoSistema)
    print("\nResultado do Sistema:")
    k = 0
    while k < tamanhoSistema:
        print(f"x{k + 1} = {resultados[k]:.2f}")
        k += 1


def pivoteamento(matriz, tamanhoSistema):
    i = 0
    while(i < tamanhoSistema):
        if(matriz[i][i] == 0):
            listaAux = []
            j = 0
            while(j < tamanhoSistema):
                if j<i:
                    listaAux.append(-1)
                else:
                    listaAux.append(abs(matriz[j][i]))
                j+=1
            indice = listaAux.index(max(listaAux))
            matriz[[i, indice]] = matriz[[indice, i]]
        i+=1
    return matriz


def escalonamento(matriz, tamanhoSistema):
    pivo = 0
    while pivo < tamanhoSistema-1:
        i = pivo + 1
        while i < tamanhoSistema:
            # 1. Calcula o multiplicador 'm' UMA vez para a linha 'i' (antes de mudar o j)
            m = matriz[i][pivo] / matriz[pivo][pivo]

            # 2. Agora percorre todas as colunas 'j' multiplicando 'm' pela linha 0
            j = 0
            while (j < tamanhoSistema + 1):
                fatorSubtrativo = m * matriz[pivo][j]
                matriz[i][j] = matriz[i][j] - fatorSubtrativo
                j += 1

            i += 1
        pivo+=1
    return matriz

def regressao(matriz, tamanhoSistema):
    # Cria um vetor de zeros para guardar os resultados [x1, x2, x3...]
    x = np.zeros(tamanhoSistema)

    # Começa da última linha (no sistema 3x3, começa no índice 2)
    i = tamanhoSistema - 1

    while i >= 0:
        soma = 0
        # Olha apenas para as colunas à direita do pivô (onde já sabemos o valor de x)
        j = i + 1
        while j < tamanhoSistema:
            soma = soma + (matriz[i][j] * x[j])
            j += 1

        # b está na coluna 'tamanhoSistema'. Subtraímos a soma e dividimos pelo pivô:
        b = matriz[i][tamanhoSistema]
        x[i] = (b - soma) / matriz[i][i]

        i -= 1  # Sobe para a linha de cima!

    return x



def imprimirMatriz(matriz, string="Matriz"):
    print(f"{string}:")
    linha = 0
    while(linha < len(matriz)):
        coluna = 0
        while(coluna < len(matriz[linha])):
            print(f"{matriz[linha][coluna]:8.2f}", end=" ")
            coluna += 1
        print()
        linha += 1

while True:
    opcaoEscolhida = int(input())
    if opcaoEscolhida != 1 and opcaoEscolhida != 2:
        print("Opcao inválida, tente novamente (1 ou 2)!")
    else:
        break

def main():
    metodoGauss(opcaoEscolhida)

if __name__ == "__main__":
    main()

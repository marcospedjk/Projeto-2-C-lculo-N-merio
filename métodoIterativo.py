import numpy as np


def verificar_dominancia_diagonal(A):

    n = len(A)
    dominante = True
    print("\n--- Verificação do Critério de Convergência (Diagonal Dominante) ---")
    for i in range(n):
        diagonal = abs(A[i][i])
        soma_outros = sum(abs(A[i][j]) for j in range(n) if j != i)
        print(f"Linha {i + 1}: |A[{i + 1}][{i + 1}]| = {diagonal:.2f} | Soma dos outros = {soma_outros:.2f}")
        if diagonal < soma_outros:
            dominante = False

    if dominante:
        print("-> A matriz é estritamente dominante na diagonal. Convergência garantida")
    else:
        print(
            "-> A matriz NÃO é estritamente dominante na diagonal. O método ainda pode convergir, mas sem garantia prévia.")
    print("-" * 65)






def gauss_seidel(A, b, x0, tol=0.0001, max_iter=1000):
    """
    Módulo do Método Iterativo de Gauss-Seidel:
    Calcula as aproximações sucessivas até atingir a tolerância estipulada.
    """
    n = len(b)
    x = np.array(x0, dtype=float)

    print(f"\nAproximação Inicial (x0): {np.round(x, 6)}")
    print("=" * 65)
    print(f"{'Iteração':<10} | {'Soluções (x)':<42} | {'Erro Máximo':<10}")
    print("=" * 65)

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            # Soma dos termos anteriores já atualizados na mesma iteração
            soma1 = sum(A[i][j] * x[j] for j in range(i))
            # Soma dos termos restantes da iteração anterior
            soma2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))

            if A[i][i] == 0:
                raise ValueError(f"Zero encontrado na diagonal principal (linha {i + 1}). O método falha.")

            x[i] = (b[i] - soma1 - soma2) / A[i][i]

        # Cálculo do erro absoluto máximo entre sucessivas iterações
        erro = np.max(np.abs(x - x_old))

        # Exibe a linha da iteração formatada
        x_str = ", ".join([f"{val:10.5f}" for val in x])
        print(f"{k + 1:<10} | [{x_str}] | {erro:.6f}")

        # Critério de Parada
        if erro < tol:
            print("=" * 65)
            print(f"Sucesso: Convergência atingida na iteração {k + 1} (Erro < {tol})!")
            return x

    print("=" * 65)
    print("Aviso: Número máximo de iterações atingido sem convergência estrita.")
    return x


def executar_questao_problema():
    """
    Módulo do Problema Padrão:
    Carrega os dados específicos da Questão 3 do Tópico 02 (Circuito Elétrico).
    """
    print("\n>>> EXECUTANDO: Tópico 02, Questão 3 (Circuito Elétrico de 5 Malhas) <<<")

    # Matriz de coeficientes (Resistências obtidas pelas Leis de Kirchhoff)
    A = np.array([
        [9.5, -2.5, 0.0, -2.0, 0.0],
        [-2.5, 11.0, -3.5, 0.0, -5.0],
        [0.0, -3.5, 15.5, 0.0, -4.0],
        [-2.0, 0.0, 0.0, 9.0, -3.0],
        [0.0, -5.0, -4.0, -3.0, 16.0]
    ], dtype=float)

    # Vetor de termos independentes (Fontes de tensão)
    b = np.array([12.0, 16.0, 14.0, 10.0, 30.0], dtype=float)

    # 1. Verifica o critério de convergência
    verificar_dominancia_diagonal(A)

    # 2. Define a aproximação inicial exigida pelo enunciado: b_i / a_ii
    x0 = b / np.diagonal(A)
    tol = 0.0001

    # 3. Executa o método iterativo
    correntes = gauss_seidel(A, b, x0, tol=tol)

    print("\n[RESULTADO FINAL] Correntes de Malha Encontradas:")
    for i, curr in enumerate(correntes, 1):
        print(f"  i{i} = {curr:.4f} A")


def executar_sistema_personalizado():
    """
    Módulo de Entrada Personalizada:
    Permite ao usuário entrar com qualquer matriz e vetor para testar outros problemas.
    """
    print("\n>>> EXECUTANDO: Resolução de Sistema Personalizado <<<")
    try:
        n = int(input("Digite o número de equações/variáveis (ex: 3): "))
        if n <= 0:
            print("O tamanho do sistema deve ser um número positivo.")
            return

        print("Digite os coeficientes da matriz A linha por linha (separados por espaço):")
        A = []
        for i in range(n):
            linha = list(map(float, input(f"Linha {i + 1}: ").split()))
            if len(linha) != n:
                print("Erro: A quantidade de colunas deve ser igual ao número de variáveis.")
                return
            A.append(linha)
        A = np.array(A, dtype=float)

        print("Digite os elementos do vetor b (termos independentes) separados por espaço:")
        b = list(map(float, input("b = ").split()))
        if len(b) != n:
            print("Erro: O tamanho do vetor b deve corresponder ao número de equações.")
            return
        b = np.array(b, dtype=float)

        tol = float(input("Digite a tolerância desejada (ex: 0.0001): "))

        # Verifica convergência
        verificar_dominancia_diagonal(A)

        escolha_x0 = input("Deseja usar a aproximação inicial padrão (b_i / a_ii)? (s/n): ").strip().lower()
        if escolha_x0 == 's':
            x0 = b / np.diagonal(A)
        else:
            x0 = list(map(float, input("Digite os valores iniciais separados por espaço: ").split()))
            if len(x0) != n:
                print("Erro: Tamanho incorreto para o vetor de aproximação inicial.")
                return

        resultado = gauss_seidel(A, b, x0, tol=tol)

        print("\n[RESULTADO FINAL] Solução do Sistema:")
        for i, val in enumerate(resultado, 1):
            print(f"  x{i} = {val:.6f}")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")




def menu_principal():

    print("\n" + "=" * 65)
    print("   SISTEMA DE CÁLCULO NUMÉRICO - MÉTODO DE GAUSS-SEIDEL")
    print("=" * 65)
    print("[1] Resolver a Questão 3 do Tópico 02 (Circuito do Problema)")
    print("[2] Inserir dados para resolver outro sistema personalizado")
    print("[3] Sair do Programa")
    print("=" * 65)


def main():
    """
    Função Principal (Main):
    """
    while True:
        menu_principal()
        try:
            opcao = int(input("Escolha uma opção (1-3): "))
            if opcao == 1:
                executar_questao_problema()
            elif opcao == 2:
                executar_sistema_personalizado()
            elif opcao == 3:
                print("\nEncerrando o programa.")
                break
            else:
                print("\nOpção inválida! Por favor, escolha entre 1, 2 e 3.")
        except ValueError:
            print("\nEntrada inválida! Digite um número inteiro correspondente à opção.")


if __name__ == "__main__":
    main()
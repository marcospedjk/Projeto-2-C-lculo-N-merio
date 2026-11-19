import numpy as np


def calcular_erro_quadratico(y_real, y_pred):
    """
    Calcula o erro quadrático cometido: E = sum((y_real - y_pred)^2)
    """
    return np.sum((y_real - y_pred) ** 2)


def ajustar_reta(x, y):
    """
    Módulo de Ajuste Linear (Reta): G(x) = a0 + a1*x
    """
    # np.polyfit com grau 1 retorna os coeficientes [a1, a0]
    coefs = np.polyfit(x, y, 1)
    a1, a0 = coefs[0], coefs[1]

    # Função geradora do modelo
    y_pred = a0 + a1 * x
    erro = calcular_erro_quadratico(y, y_pred)

    print("\n--- [1] Ajuste por Reta (Linear) ---")
    print(f"Equação: G(x) = {a0:.4f} + {a1:.4f}*x")
    print(f"Erro Quadrático Cometido (E): {erro:.6f}")
    return y_pred, erro


def ajustar_parabola(x, y):
    """
    Módulo de Ajuste Parabólico (Polinomial de 2º Grau): G(x) = a0 + a1*x + a2*x^2
    """
    # np.polyfit com grau 2 retorna [a2, a1, a0]
    coefs = np.polyfit(x, y, 2)
    a2, a1, a0 = coefs[0], coefs[1], coefs[2]

    y_pred = a0 + a1 * x + a2 * (x ** 2)
    erro = calcular_erro_quadratico(y, y_pred)

    print("\n--- [2] Ajuste por Parábola (2º Grau) ---")
    print(f"Equação: G(x) = {a0:.4f} + {a1:.4f}*x + {a2:.4f}*x^2")
    print(f"Erro Quadrático Cometido (E): {erro:.6f}")
    return y_pred, erro


def ajustar_exponencial(x, y):
    """
    Módulo de Ajuste Exponencial: G(x) = a * e^(b*x)
    Linearização: ln(y) = ln(a) + b*x
    """
    # Como aplicamos ln(y), garantimos que y > 0
    ln_y = np.log(y)

    # Ajuste linear nos dados transformados: [b, ln(a)]
    coefs = np.polyfit(x, ln_y, 1)
    b, ln_a = coefs[0], coefs[1]
    a = np.exp(ln_a)

    y_pred = a * np.exp(b * x)
    erro = calcular_erro_quadratico(y, y_pred)

    print("\n--- [3] Ajuste por Exponencial ---")
    print(f"Equação: G(x) = {a:.4f} * e^({b:.4f}*x)")
    print(f"Erro Quadrático Cometido (E): {erro:.6f}")
    return y_pred, erro


def executar_questao_problema():
    """
    Carrega os dados específicos da Questão 3 do Tópico 03.
    """
    print("\n>>> EXECUTANDO: Tópico 03, Questão 3 (Regressão por Mínimos Quadrados) <<<")

    # Dados da tabela fornecida na imagem
    x = np.array([0, 1.5, 2.6, 4.2, 6, 8.2, 10, 11.4], dtype=float)
    F_x = np.array([18, 13, 11, 9, 6, 4, 2, 1], dtype=float)

    print("\nPontos Originais:")
    print(f"x = {x.tolist()}")
    print(f"F(x) = {F_x.tolist()}")
    print("=" * 65)

    # Executa os três ajustes
    _, erro_reta = ajustar_reta(x, F_x)
    _, erro_parab = ajustar_parabola(x, F_x)
    _, erro_exp = ajustar_exponencial(x, F_x)

    print("=" * 65)
    print("RESUMO COMPARATIVO DOS ERROS:")
    print(f" * Erro da Reta:      {erro_reta:.6f}")
    print(f" * Erro da Parábola:  {erro_parab:.6f}")
    print(f" * Erro Exponencial:  {erro_exp:.6f}")

    # Identifica o melhor ajuste com base no menor erro quadrático
    erros = {"Reta": erro_reta, "Parábola": erro_parab, "Exponencial": erro_exp}
    melhor = min(erros, key=erros.get)
    print(f"\n-> Conclusão: O melhor ajuste para este conjunto de dados foi a **{melhor}** (menor erro quadrático).")
    print("=" * 65)


def executar_sistema_personalizado():
    """
    Permite ao usuário inserir dados arbitrários para testar outros problemas de mínimos quadrados.
    """
    print("\n>>> EXECUTANDO: Regressão por Mínimos Quadrados (Dados Personalizados) <<<")
    try:
        entrada_x = input("Digite os valores de x separados por espaço (ex: 1 2 3 4): ")
        x = np.array([float(val) for val in entrada_x.split()], dtype=float)

        entrada_y = input("Digite os valores de F(x) correspondentes separados por espaço (ex: 2 4 5 4): ")
        y = np.array([float(val) for val in entrada_y.split()], dtype=float)

        if len(x) != len(y) or len(x) == 0:
            print("Erro: Os vetores x e y devem ter o mesmo tamanho e não podem estar vazios.")
            return

        print("\nProcessando ajustes...")
        _, erro_reta = ajustar_reta(x, y)
        _, erro_parab = ajustar_parabola(x, y)

        # Verifica se há valores menores ou iguais a zero para a exponencial
        if np.any(y <= 0):
            print("\n--- [3] Ajuste por Exponencial ---")
            print(
                "Aviso: O ajuste exponencial foi ignorado pois existem valores de F(x) <= 0 (o logaritmo não é real).")
        else:
            ajustar_exponencial(x, y)

        print("=" * 65)

    except Exception as e:
        print(f"Ocorreu um erro durante a entrada de dados: {e}")



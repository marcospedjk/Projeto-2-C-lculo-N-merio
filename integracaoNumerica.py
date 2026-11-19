# Integração Numérica - Regra dos Trapézios Repetida e Regra 1/3 de Simpson Repetida

import numpy as np


def integracaoNumerica(opcaoEscolhida):
    espacamentoConstante = True

    if opcaoEscolhida == 1:
        # Problema proposto: área da seção do trecho mais largo de um navio
        # Pontos de A (x0 = 0.0) até A7 (x7 = 2.8), com h = 0.4 e 7 subintervalos
        h = 0.4
        y = np.array([3.00, 2.92, 2.75, 2.52, 2.30, 1.84, 0.92, 0.00], dtype=float)
        n = len(y) - 1
        x = np.zeros(n + 1)
        i = 0
        while i <= n:
            x[i] = i * h
            i += 1

    elif opcaoEscolhida == 2:
        # Entrada com espaçamento h e valores de f(x)
        while True:
            qtdPontos = int(input("Quantos pontos você deseja inserir (mínimo 2): "))
            if qtdPontos < 2:
                print("É necessário pelo menos 2 pontos (1 subintervalo).")
            else:
                break

        while True:
            h = float(input("Qual o valor do espaçamento (h): "))
            if h <= 0:
                print("O espaçamento h deve ser um valor positivo.")
            else:
                break

        x0 = float(input("Qual o valor inicial x0 (digite 0 se não informado): "))

        n = qtdPontos - 1
        x = np.zeros(qtdPontos)
        y = np.zeros(qtdPontos)

        i = 0
        print("\nInsira os valores de f(x) para cada ponto:")
        while i < qtdPontos:
            x[i] = x0 + i * h
            y[i] = float(input(f"f(x{i}) [x{i} = {x[i]:.4f}]: "))
            i += 1

    elif opcaoEscolhida == 3:
        # Entrada direta com os pares de pontos (x_i, f(x_i))
        while True:
            qtdPontos = int(input("Quantos pontos (x, f(x)) você deseja inserir (mínimo 2): "))
            if qtdPontos < 2:
                print("É necessário pelo menos 2 pontos (1 subintervalo).")
            else:
                break

        x = np.zeros(qtdPontos)
        y = np.zeros(qtdPontos)

        i = 0
        print("\nInsira os pontos em ordem crescente de x:")
        while i < qtdPontos:
            print(f"\nPonto {i}:")
            while True:
                valorX = float(input(f"  x{i}: "))
                if i > 0 and valorX <= x[i - 1]:
                    print(f"  O valor de x{i} deve ser maior que x{i - 1} ({x[i - 1]}).")
                else:
                    x[i] = valorX
                    break
            y[i] = float(input(f"  f(x{i}): "))
            i += 1

        espacamentoConstante, h = verificarEspacamento(x)

    else:
        # Entrada com função f(x), intervalo [a, b] e número de subintervalos
        print("\nDica: use x como variável.")
        print("Exemplos: 1/x  |  x*exp(x) + 1  |  (1 + x**2)**(-0.5)  |  ln(x)")
        funcaoStr = input("Digite a função f(x): ")

        a = float(input("Limite inferior (a): "))
        while True:
            b = float(input("Limite superior (b): "))
            if b <= a:
                print("O limite superior (b) deve ser maior que o limite inferior (a).")
            else:
                break

        while True:
            n = int(input("Número de subintervalos (n): "))
            if n < 1:
                print("O número de subintervalos deve ser um inteiro positivo.")
            else:
                break

        h = (b - a) / n
        x = np.zeros(n + 1)
        y = np.zeros(n + 1)

        i = 0
        while i <= n:
            x[i] = a + i * h
            y[i] = avaliarFuncao(funcaoStr, x[i])
            i += 1

    imprimirTabela(x, y, h, espacamentoConstante)

    # 1. Regra dos Trapézios Repetida
    if espacamentoConstante:
        resultadoTrapezio = regraTrapeziosRepetida(y, h)
    else:
        resultadoTrapezio = regraTrapeziosVariavel(x, y)
    print(f"\nResultado - Regra dos Trapézios Repetida: {resultadoTrapezio:.4f}")

    # 2. Regra 1/3 de Simpson Repetida
    if espacamentoConstante:
        resultadoSimpson = regraSimpsonRepetida(y, h)
        if resultadoSimpson is not None:
            print(f"Resultado - Regra 1/3 de Simpson Repetida: {resultadoSimpson:.4f}")
    else:
        print("\nAviso: Os pontos informados não possuem espaçamento (h) constante.")
        print("A Regra 1/3 de Simpson Repetida exige subintervalos de mesma amplitude h.")


def verificarEspacamento(x):
    hBase = x[1] - x[0]
    tolerancia = 1e-6
    i = 1
    while i < len(x) - 1:
        hAtual = x[i + 1] - x[i]
        if abs(hAtual - hBase) > tolerancia:
            return False, None
        i += 1
    return True, hBase


def avaliarFuncao(funcaoStr, valorX):
    # Permite usar '^' para potência e 'ln' para logaritmo natural
    expressao = funcaoStr.replace("^", "**")
    ambienteSeguro = {
        "x": valorX,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "exp": np.exp,
        "log": np.log,
        "ln": np.log,
        "log10": np.log10,
        "sqrt": np.sqrt,
        "abs": abs,
        "pi": np.pi,
        "e": np.e
    }
    return float(eval(expressao, {"__builtins__": None}, ambienteSeguro))


def regraTrapeziosRepetida(y, h):
    n = len(y) - 1
    somaInternos = 0.0

    # Soma todos os termos internos: f(x1) até f(xn-1)
    i = 1
    while i < n:
        somaInternos = somaInternos + y[i]
        i += 1

    # Fórmula: (h / 2) * (f(x0) + 2 * somaInternos + f(xn))
    area = (h / 2.0) * (y[0] + (2.0 * somaInternos) + y[n])
    return area


def regraTrapeziosVariavel(x, y):
    # Soma a área de cada trapézio individual quando h não é constante
    n = len(y) - 1
    areaTotal = 0.0
    i = 0
    while i < n:
        hAtual = x[i + 1] - x[i]
        areaTotal = areaTotal + (hAtual / 2.0) * (y[i] + y[i + 1])
        i += 1
    return areaTotal


def regraSimpsonRepetida(y, h):
    n = len(y) - 1

    if n < 2:
        print("\nAviso: A Regra 1/3 de Simpson exige pelo menos 2 subintervalos (3 pontos).")
        return None

    # Se n for ímpar, aplica Simpson nos primeiros (n - 1) subintervalos
    # e Trapézio Simples no último subintervalo
    if n % 2 != 0:
        limiteSimpson = n - 1
        areaUltimoTrapezio = (h / 2.0) * (y[n - 1] + y[n])
    else:
        limiteSimpson = n
        areaUltimoTrapezio = 0.0

    somaImpares = 0.0
    somaPares = 0.0

    # Percorre os pontos internos do trecho de Simpson (de 1 até limiteSimpson - 1)
    i = 1
    while i < limiteSimpson:
        if i % 2 != 0:
            somaImpares = somaImpares + y[i]
        else:
            somaPares = somaPares + y[i]
        i += 1

    # Fórmula: (h / 3) * (f(x0) + 4*somaImpares + 2*somaPares + f(x_limite))
    areaSimpson = (h / 3.0) * (y[0] + (4.0 * somaImpares) + (2.0 * somaPares) + y[limiteSimpson])

    return areaSimpson + areaUltimoTrapezio


def imprimirTabela(x, y, h, espacamentoConstante):
    if espacamentoConstante:
        print(f"\nTabela de Pontos (n = {len(y) - 1} subintervalos | h = {h:.4f}):")
    else:
        print(f"\nTabela de Pontos (n = {len(y) - 1} subintervalos | h variável):")

    print(f"{'i':>4} | {'x_i':>10} | {'f(x_i)':>10}")
    print("-" * 30)
    i = 0
    while i < len(y):
        print(f"{i:4d} | {x[i]:10.4f} | {y[i]:10.4f}")
        i += 1


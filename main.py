# Menu Principal - Projeto de Cálculo Numérico

import sistemasLineares_metodosDiretos as gauss
import metodoIterativo as gauss_seidel
import minimosQuadrados as minimos_quadrados
import integracaoNumerica as integracao


def lerOpcao(minimo, maximo):
    while True:
        try:
            opcao = int(input(f"Escolha uma opção ({minimo}-{maximo}): "))
            if minimo <= opcao <= maximo:
                return opcao
            else:
                print(f"Opção inválida! Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def menuGauss():
    print("\n" + "-" * 65)
    print("   TÓPICO 01 - SISTEMAS LINEARES (MÉTODO DIRETO DE GAUSS)")
    print("-" * 65)
    print("[1] Problema proposto")
    print("[2] Fornecer sistema personalizado")
    print("[3] Voltar ao menu principal")

    opcao = lerOpcao(1, 3)
    if opcao != 3:
        gauss.metodoGauss(opcao)


def menuGaussSeidel():
    print("\n" + "-" * 65)
    print("   TÓPICO 02 - SISTEMAS LINEARES (MÉTODO ITERATIVO GAUSS-SEIDEL)")
    print("-" * 65)
    print("[1] Resolver a Questão 3 do Tópico 02 (Circuito Elétrico)")
    print("[2] Inserir dados para resolver outro sistema personalizado")
    print("[3] Voltar ao menu principal")

    opcao = lerOpcao(1, 3)
    if opcao == 1:
        gauss_seidel.executar_questao_problema()
    elif opcao == 2:
        gauss_seidel.executar_sistema_personalizado()


def menuMinimosQuadrados():
    print("\n" + "-" * 65)
    print("   TÓPICO 03 - AJUSTE DE CURVAS (MÍNIMOS QUADRADOS)")
    print("-" * 65)
    print("[1] Resolver a Questão 3 do Tópico 03 (Dados da Tabela)")
    print("[2] Inserir dados personalizados para nova regressão")
    print("[3] Voltar ao menu principal")

    opcao = lerOpcao(1, 3)
    if opcao == 1:
        minimos_quadrados.executar_questao_problema()
    elif opcao == 2:
        minimos_quadrados.executar_sistema_personalizado()


def menuIntegracao():
    print("\n" + "-" * 65)
    print("   TÓPICO 04 - INTEGRAÇÃO NUMÉRICA (TRAPÉZIOS E 1/3 DE SIMPSON)")
    print("-" * 65)
    print("[1] Problema proposto (área da seção do navio)")
    print("[2] Fornecer valores de f(x) e espaçamento (h)")
    print("[3] Fornecer pontos (x, f(x)) diretamente")
    print("[4] Fornecer função f(x) e intervalo [a, b]")
    print("[5] Voltar ao menu principal")

    opcao = lerOpcao(1, 5)
    if opcao != 5:
        integracao.integracaoNumerica(opcao)


def main():
    while True:
        print("\n" + "=" * 65)
        print("          SISTEMA DE CÁLCULO NUMÉRICO - MENU PRINCIPAL")
        print("=" * 65)
        print("[1] Tópico 01 - Método Direto de Gauss")
        print("[2] Tópico 02 - Método Iterativo de Gauss-Seidel")
        print("[3] Tópico 03 - Regressão por Mínimos Quadrados")
        print("[4] Tópico 04 - Integração Numérica")
        print("[5] Sair do Programa")
        print("=" * 65)

        opcao = lerOpcao(1, 5)

        if opcao == 1:
            menuGauss()
        elif opcao == 2:
            menuGaussSeidel()
        elif opcao == 3:
            menuMinimosQuadrados()
        elif opcao == 4:
            menuIntegracao()
        elif opcao == 5:
            print("\nEncerrando o programa. Bom trabalho na apresentação!")
            break


if __name__ == "__main__":
    main()
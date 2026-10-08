"""Simulador Financeiro
Calcula parcelas de financiamento (Tabela Price), rendimento de
investimentos com juros compostos e gera a tabela de amortização em CSV.
"""

import csv


def calcular_parcela(valor, taxa_mensal, meses):
    """Retorna o valor da parcela fixa (Tabela Price).
    taxa_mensal é decimal: 1% = 0.01."""
    if meses <= 0:
        raise ValueError("O número de meses deve ser maior que zero.")
    if taxa_mensal == 0:
        return valor / meses
    return valor * taxa_mensal / (1 - (1 + taxa_mensal) ** -meses)


def calcular_montante(capital, taxa_mensal, meses):
    """Retorna o montante com juros compostos, sem aportes mensais."""
    return capital * (1 + taxa_mensal) ** meses


def calcular_montante_com_aportes(capital, aporte, taxa_mensal, meses):
    """Retorna o montante com aportes feitos no final de cada mês."""
    saldo = capital
    for _ in range(meses):
        saldo = saldo * (1 + taxa_mensal) + aporte
    return saldo


def gerar_tabela_amortizacao(valor, taxa_mensal, meses):
    """Retorna uma lista de linhas: [mes, parcela, juros, amortizacao, saldo]."""
    parcela = calcular_parcela(valor, taxa_mensal, meses)
    saldo = valor
    tabela = []
    for mes in range(1, meses + 1):
        juros = saldo * taxa_mensal
        amortizacao = parcela - juros
        saldo = saldo - amortizacao
        tabela.append([mes, parcela, juros, amortizacao, max(saldo, 0)])
    return tabela


def formatar_moeda(valor):
    """Formata um número como moeda brasileira: 1234.5 -> R$ 1.234,50"""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def salvar_csv(tabela, nome_arquivo):
    """Salva a tabela de amortização em um arquivo CSV."""
    with open(nome_arquivo, "wt", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["mes", "parcela", "juros", "amortizacao", "saldo"])
        for linha in tabela:
            escritor.writerow([linha[0]] + [f"{v:.2f}" for v in linha[1:]])


def ler_numero(mensagem):
    """Pede um número ao usuário e repete até ele digitar um valor válido."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def simular_financiamento():
    valor = ler_numero("Valor financiado (R$): ")
    taxa = ler_numero("Taxa de juros ao mês (%): ") / 100
    meses = int(ler_numero("Número de meses: "))

    try:
        parcela = calcular_parcela(valor, taxa, meses)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    total = parcela * meses
    print(f"\nParcela mensal: {formatar_moeda(parcela)}")
    print(f"Total pago: {formatar_moeda(total)}")
    print(f"Total de juros: {formatar_moeda(total - valor)}")

    resposta = input("\nSalvar tabela de amortização em CSV? (s/n): ").lower()
    if resposta == "s":
        tabela = gerar_tabela_amortizacao(valor, taxa, meses)
        salvar_csv(tabela, "amortizacao.csv")
        print("Arquivo amortizacao.csv criado.")


def simular_investimento():
    capital = ler_numero("Capital inicial (R$): ")
    aporte = ler_numero("Aporte mensal (R$): ")
    taxa = ler_numero("Rendimento ao mês (%): ") / 100
    meses = int(ler_numero("Número de meses: "))

    montante = calcular_montante_com_aportes(capital, aporte, taxa, meses)
    investido = capital + aporte * meses
    print(f"\nTotal investido: {formatar_moeda(investido)}")
    print(f"Montante final: {formatar_moeda(montante)}")
    print(f"Rendimento: {formatar_moeda(montante - investido)}")


def main():
    while True:
        print("\n=== Simulador Financeiro ===")
        print("1 - Simular financiamento")
        print("2 - Simular investimento")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            simular_financiamento()
        elif opcao == "2":
            simular_investimento()
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
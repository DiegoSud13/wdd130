# Melhorias adicionais (desafios):
# 1. Exibe quantos dias faltam para a Promoção de Ano Novo (1º de janeiro).
# 2. Exibe a data limite para devolução: 30 dias após a compra, às 21h.
# 3. Promoção "compre 1, leve o 2º com 50% de desconto" no item D083.
#    A cada 2 unidades, uma é cobrada com 50% de desconto. O desconto
#    aparece no recibo.
# 4. Imprime um cupom de 10% de desconto para um produto sorteado entre
#    os produtos que o cliente comprou.

import csv
import random
from datetime import datetime, timedelta

NOME_LOJA = "Empório Inkom"
ALIQUOTA_IMPOSTO = 0.06
PRODUTO_PROMOCAO = "D083"
PROMOCAO_ATIVA = True  # mude para False para desligar a promoção


def ler_dicionario(filename, indice_coluna_chave):
    """Lê um arquivo CSV e retorna um dicionário em que a chave é o valor
    da coluna indice_coluna_chave e o valor é a lista com a linha inteira."""
    dicionario = {}
    with open(filename, "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)  # pula a linha de títulos
        for linha in leitor:
            if len(linha) != 0:
                chave = linha[indice_coluna_chave]
                dicionario[chave] = linha
    return dicionario


def main():
    try:
        dic_produtos = ler_dicionario("produtos.csv", 0)

        print(NOME_LOJA)

        total_itens = 0
        subtotal = 0
        qtd_promocao = 0
        nomes_comprados = []

        with open("pedido.csv", "rt", encoding="utf-8") as arquivo_pedido:
            leitor = csv.reader(arquivo_pedido)
            next(leitor)  # pula a linha de títulos
            for linha in leitor:
                if len(linha) != 0:
                    num_prod = linha[0]
                    quantidade = int(linha[1])

                    produto = dic_produtos[num_prod]  # pode gerar KeyError
                    nome = produto[1]
                    preco = float(produto[2])

                    print(f"{nome}: {quantidade} @ {preco:.2f}")

                    total_itens += quantidade
                    subtotal += quantidade * preco

                    if nome not in nomes_comprados:
                        nomes_comprados.append(nome)

                    if num_prod == PRODUTO_PROMOCAO:
                        qtd_promocao += quantidade

        # Desconto: a cada 2 unidades do D083, uma sai com 50% de desconto
        desconto = 0
        if PROMOCAO_ATIVA and qtd_promocao > 0:
            preco_promocao = float(dic_produtos[PRODUTO_PROMOCAO][2])
            unidades_com_desconto = qtd_promocao // 2
            desconto = unidades_com_desconto * preco_promocao * 0.5

        subtotal_com_desconto = subtotal - desconto
        imposto = subtotal_com_desconto * ALIQUOTA_IMPOSTO
        total = subtotal_com_desconto + imposto

        print(f"Número de itens: {total_itens}")
        print(f"Subtotal: {subtotal:.2f}")
        if desconto > 0:
            print(f"Desconto (leve 2, o 2º com 50%): -{desconto:.2f}")
        print(f"Imposto sobre vendas: {imposto:.2f}")
        print(f"Total: {total:.2f}")
        print(f"Obrigado por comprar no {NOME_LOJA}.")

        agora = datetime.now()
        print(agora.strftime("%d/%m/%Y %H:%M:%S"))

        # Dias até a Promoção de Ano Novo
        ano_novo = datetime(agora.year + 1, 1, 1)
        dias_restantes = (ano_novo - agora).days
        print(f"Faltam {dias_restantes} dias para a Promoção de Ano Novo (1º de janeiro).")

        # Data limite de devolução (30 dias depois, às 21h)
        limite = (agora + timedelta(days=30)).replace(hour=21, minute=0, second=0)
        print(f"Data limite para devolução: {limite.strftime('%d/%m/%Y %H:%M:%S')}")

        # Cupom de desconto para um produto que o cliente comprou
        produto_cupom = random.choice(nomes_comprados)
        print(f"CUPOM: 10% de desconto em '{produto_cupom}' na próxima compra!")

    except FileNotFoundError as erro:
        print("Error: missing file")
        print(erro)

    except PermissionError as erro:
        print("Error: permission denied")
        print(erro)

    except KeyError as erro:
        print("Error: unknown product ID in the request.csv file")
        print(erro)


if __name__ == "__main__":
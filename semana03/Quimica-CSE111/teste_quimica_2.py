from quimica import (
    criar_tabela_periodica,
    calcular_massa_molar
)

from formula import interpretar_formula


def test_criar_tabela_periodica():
    tabela = criar_tabela_periodica()

    assert "H" in tabela
    assert "C" in tabela
    assert "O" in tabela

    assert tabela["H"][0] == "Hidrogênio"
    assert tabela["C"][0] == "Carbono"
    assert tabela["O"][0] == "Oxigênio"


def test_interpretar_formula():
    resultado = interpretar_formula("C6H12O6")

    esperado = [
        ["C", 6],
        ["H", 12],
        ["O", 6]
    ]

    assert resultado == esperado


def test_calcular_massa_molar():
    tabela = criar_tabela_periodica()

    lista = [
        ["H", 2],
        ["O", 1]
    ]

    massa = calcular_massa_molar(
        lista,
        tabela
    )

    assert abs(massa - 18.015) < 0.01
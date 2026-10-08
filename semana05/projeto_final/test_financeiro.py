import csv
import pytest
from financeiro import (
    calcular_parcela,
    calcular_montante,
    calcular_montante_com_aportes,
    gerar_tabela_amortizacao,
    formatar_moeda,
    salvar_csv,
)


def test_calcular_parcela():
    assert calcular_parcela(1000, 0.01, 12) == pytest.approx(88.85, abs=0.01)
    assert calcular_parcela(1200, 0, 12) == pytest.approx(100)


def test_calcular_parcela_meses_invalidos():
    with pytest.raises(ValueError):
        calcular_parcela(1000, 0.01, 0)


def test_calcular_montante():
    assert calcular_montante(1000, 0.01, 12) == pytest.approx(1126.83, abs=0.01)
    assert calcular_montante(1000, 0, 12) == pytest.approx(1000)


def test_calcular_montante_com_aportes():
    assert calcular_montante_com_aportes(0, 100, 0, 12) == pytest.approx(1200)
    assert calcular_montante_com_aportes(0, 100, 0.01, 12) == pytest.approx(1268.25, abs=0.01)


def test_gerar_tabela_amortizacao():
    tabela = gerar_tabela_amortizacao(1000, 0.01, 12)
    assert len(tabela) == 12
    assert tabela[-1][4] == pytest.approx(0, abs=0.01)
    assert sum(linha[3] for linha in tabela) == pytest.approx(1000, abs=0.01)


def test_formatar_moeda():
    assert formatar_moeda(1234.5) == "R$ 1.234,50"
    assert formatar_moeda(0) == "R$ 0,00"
    assert formatar_moeda(1000000) == "R$ 1.000.000,00"


def test_salvar_csv(tmp_path):
    tabela = gerar_tabela_amortizacao(1000, 0.01, 3)
    arquivo = tmp_path / "teste.csv"
    salvar_csv(tabela, str(arquivo))

    with open(arquivo, "rt", encoding="utf-8") as f:
        linhas = list(csv.reader(f))

    assert linhas[0] == ["mes", "parcela", "juros", "amortizacao", "saldo"]
    assert len(linhas) == 4  # título + 3 meses


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
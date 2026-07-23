# Melhoria adicional:
# O programa utiliza constantes para a gravidade, densidade da água
# e viscosidade dinâmica, evitando repetir valores dentro das funções.
# Também foi adicionada a conversão de kPa para MCA.

ACELERACAO_DA_GRAVIDADE_TERRA = 9.8066500
DENSIDADE_AGUA = 998.2000000
VISCOSIDADE_DINAMICA_AGUA = 0.0010016


def calc_altura_coluna_agua(altura_torre, altura_tanque):
    """Calcula a altura da coluna de água."""
    return altura_torre + (3 * altura_tanque / 4)


def calc_pressao_pela_altura(altura):
    """Calcula a pressão causada pela altura da água."""
    return (
        DENSIDADE_AGUA
        * ACELERACAO_DA_GRAVIDADE_TERRA
        * altura
        / 1000
    )


def calc_perda_pressao_tubo(
    diametro_tubo,
    comprimento_tubo,
    fator_atrito,
    velocidade_fluido
):
    """Calcula a perda de pressão ao longo do tubo."""
    return -(
        fator_atrito
        * comprimento_tubo
        * DENSIDADE_AGUA
        * velocidade_fluido ** 2
    ) / (2000 * diametro_tubo)


def calc_perda_pressao_conexoes(
    velocidade_fluido,
    quantidade_conexoes
):
    """Calcula a perda de pressão nas conexões."""
    return -(
        0.04
        * DENSIDADE_AGUA
        * velocidade_fluido ** 2
        * quantidade_conexoes
    ) / 2000


def calc_num_reynolds(
    diametro_hidraulico,
    velocidade_fluido
):
    """Calcula o número de Reynolds."""
    return (
        DENSIDADE_AGUA
        * diametro_hidraulico
        * velocidade_fluido
        / VISCOSIDADE_DINAMICA_AGUA
    )


def calc_perda_pressao_reducao_tubo(
    diametro_maior,
    velocidade_fluido,
    calc_num_reynolds,
    diametro_menor
):
    """Calcula a perda de pressão causada pela redução do tubo."""

    numero_reynolds = calc_num_reynolds

    k = (
        0.1 + (50 / numero_reynolds)
    ) * (
        (diametro_maior / diametro_menor) ** 4 - 1
    )

    return -(
        k
        * DENSIDADE_AGUA
        * velocidade_fluido ** 2
    ) / 2000


def calc_kpa_para_mca(pressao_kpa):
    """Converte quilopascal para metros de coluna de água."""
    return pressao_kpa / 9.80665


def main():

    altura_torre = float(
        input("Altura da torre de água (metros): ")
    )

    altura_tanque = float(
        input(
            "Altura das paredes do tanque de água (metros): "
        )
    )

    comprimento_tubo_tanque = float(
        input(
            "Comprimento do tubo de abastecimento, "
            "do tanque até o terreno (metros): "
        )
    )

    quantidade_conexoes = int(
        input(
            "Número de ângulos de 90° no tubo de abastecimento: "
        )
    )

    comprimento_tubo_casa = float(
        input(
            "Comprimento do tubo de abastecimento "
            "até a casa (metros): "
        )
    )

    altura_coluna = calc_altura_coluna_agua(
        altura_torre,
        altura_tanque
    )

    pressao_altura = calc_pressao_pela_altura(
        altura_coluna
    )

    velocidade_fluido = 1.65

    diametro_tubo = 0.286870

    fator_atrito = 0.013

    perda_tubo_tanque = calc_perda_pressao_tubo(
        diametro_tubo,
        comprimento_tubo_tanque,
        fator_atrito,
        velocidade_fluido
    )

    perda_conexoes = calc_perda_pressao_conexoes(
        velocidade_fluido,
        quantidade_conexoes
    )

    perda_tubo_casa = calc_perda_pressao_tubo(
        diametro_tubo,
        comprimento_tubo_casa,
        fator_atrito,
        velocidade_fluido
    )

    pressao_final = (
        pressao_altura
        + perda_tubo_tanque
        + perda_conexoes
        + perda_tubo_casa
    )

    pressao_mca = calc_kpa_para_mca(
        pressao_final
    )

    print(
        f"Pressão na casa: "
        f"{pressao_final:.1f} quilopascal"
    )

    print(
        f"Pressão na casa: "
        f"{pressao_mca:.1f} MCA"
    )


if __name__ == "__main__":
    main()
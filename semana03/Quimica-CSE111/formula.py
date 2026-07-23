class FormulaError(Exception):
    """Indica que uma fórmula química possui um formato inválido."""
    pass


def interpretar_formula(formula):
    """
    Converte uma fórmula química em uma lista de símbolos e quantidades.

    Exemplo:
    C6H12O6
    retorna:
    [["C", 6], ["H", 12], ["O", 6]]
    """

    lista_quantidade_simbolos = []

    i = 0

    while i < len(formula):

        if not formula[i].isalpha() or not formula[i].isupper():
            raise FormulaError("A fórmula contém um símbolo inválido.")

        simbolo = formula[i]
        i += 1

        if i < len(formula) and formula[i].islower():
            simbolo += formula[i]
            i += 1

        quantidade = ""

        while i < len(formula) and formula[i].isdigit():
            quantidade += formula[i]
            i += 1

        if quantidade == "":
            quantidade = 1
        else:
            quantidade = int(quantidade)

        lista_quantidade_simbolos.append(
            [simbolo, quantidade]
        )

    return lista_quantidade_simbolos
from formula import interpretar_formula


def criar_tabela_periodica():
    """Retorna um dicionário contendo todos os elementos da tabela periódica."""

    tabela_periodica = {
        "H": ["Hidrogênio", 1.008],
        "He": ["Hélio", 4.002602],
        "Li": ["Lítio", 6.94],
        "Be": ["Berílio", 9.0121831],
        "B": ["Boro", 10.81],
        "C": ["Carbono", 12.011],
        "N": ["Nitrogênio", 14.007],
        "O": ["Oxigênio", 15.999],
        "F": ["Flúor", 18.998403163],
        "Ne": ["Neônio", 20.1797],
        "Na": ["Sódio", 22.98976928],
        "Mg": ["Magnésio", 24.305],
        "Al": ["Alumínio", 26.9815385],
        "Si": ["Silício", 28.085],
        "P": ["Fósforo", 30.973761998],
        "S": ["Enxofre", 32.06],
        "Cl": ["Cloro", 35.45],
        "Ar": ["Argônio", 39.948],
        "K": ["Potássio", 39.0983],
        "Ca": ["Cálcio", 40.078],
        "Sc": ["Escândio", 44.955908],
        "Ti": ["Titânio", 47.867],
        "V": ["Vanádio", 50.9415],
        "Cr": ["Cromo", 51.9961],
        "Mn": ["Manganês", 54.938044],
        "Fe": ["Ferro", 55.845],
        "Co": ["Cobalto", 58.933194],
        "Ni": ["Níquel", 58.6934],
        "Cu": ["Cobre", 63.546],
        "Zn": ["Zinco", 65.38],
        "Ga": ["Gálio", 69.723],
        "Ge": ["Germânio", 72.63],
        "As": ["Arsênio", 74.921595],
        "Se": ["Selênio", 78.971],
        "Br": ["Bromo", 79.904],
        "Kr": ["Criptônio", 83.798],
        "Rb": ["Rubídio", 85.4678],
        "Sr": ["Estrôncio", 87.62],
        "Y": ["Ítrio", 88.90584],
        "Zr": ["Zircônio", 91.224],
        "Nb": ["Nióbio", 92.90637],
        "Mo": ["Molibdênio", 95.95],
        "Tc": ["Tecnécio", 98],
        "Ru": ["Rutênio", 101.07],
        "Rh": ["Ródio", 102.9055],
        "Pd": ["Paládio", 106.42],
        "Ag": ["Prata", 107.8682],
        "Cd": ["Cádmio", 112.414],
        "In": ["Índio", 114.818],
        "Sn": ["Estanho", 118.71],
        "Sb": ["Antimônio", 121.76],
        "Te": ["Telúrio", 127.6],
        "I": ["Iodo", 126.90447],
        "Xe": ["Xenônio", 131.293],
        "Cs": ["Césio", 132.90545196],
        "Ba": ["Bário", 137.327],
        "La": ["Lantânio", 138.90547],
        "Ce": ["Cério", 140.116],
        "Pr": ["Praseodímio", 140.90766],
        "Nd": ["Neodímio", 144.242],
        "Pm": ["Promécio", 145],
        "Sm": ["Samário", 150.36],
        "Eu": ["Európio", 151.964],
        "Gd": ["Gadolínio", 157.25],
        "Tb": ["Térbio", 158.92535],
        "Dy": ["Disprósio", 162.5],
        "Ho": ["Hólmio", 164.93033],
        "Er": ["Érbio", 167.259],
        "Tm": ["Túlio", 168.93422],
        "Yb": ["Itérbio", 173.045],
        "Lu": ["Lutécio", 174.9668],
        "Hf": ["Háfnio", 178.49],
        "Ta": ["Tântalo", 180.94788],
        "W": ["Tungstênio", 183.84],
        "Re": ["Rênio", 186.207],
        "Os": ["Ósmio", 190.23],
        "Ir": ["Irídio", 192.217],
        "Pt": ["Platina", 195.084],
        "Au": ["Ouro", 196.966569],
        "Hg": ["Mercúrio", 200.592],
        "Tl": ["Tálio", 204.38],
        "Pb": ["Chumbo", 207.2],
        "Bi": ["Bismuto", 208.9804],
        "Po": ["Polônio", 209],
        "At": ["Astato", 210],
        "Rn": ["Radônio", 222],
        "Fr": ["Frâncio", 223],
        "Ra": ["Rádio", 226],
        "Ac": ["Actínio", 227],
        "Th": ["Tório", 232.0377],
        "Pa": ["Protactínio", 231.03588],
        "U": ["Urânio", 238.02891],
        "Np": ["Netúnio", 237],
        "Pu": ["Plutônio", 244],
        "Am": ["Amerício", 243],
        "Cm": ["Cúrio", 247],
        "Bk": ["Berquélio", 247],
        "Cf": ["Califórnio", 251],
        "Es": ["Einstênio", 252],
        "Fm": ["Férmio", 257],
        "Md": ["Mendelévio", 258],
        "No": ["Nobélio", 259],
        "Lr": ["Laurêncio", 262],
        "Rf": ["Rutherfórdio", 267],
        "Db": ["Dúbnio", 268],
        "Sg": ["Seabórgio", 269],
        "Bh": ["Bóhrio", 270],
        "Hs": ["Hássio", 269],
        "Mt": ["Meitnério", 278],
        "Ds": ["Darmstádtio", 281],
        "Rg": ["Roentgênio", 282],
        "Cn": ["Copernício", 285],
        "Nh": ["Nihônio", 286],
        "Fl": ["Fleróvio", 289],
        "Mc": ["Moscóvio", 290],
        "Lv": ["Livermório", 293],
        "Ts": ["Tenessino", 294],
        "Og": ["Oganessônio", 294]
    }

    return tabela_periodica


def calcular_massa_molar(lista_quantidade_simbolos, dic_da_tabela_periodica):
    """Calcula e retorna a massa molar total do composto."""

    massa_total = 0

    for item in lista_quantidade_simbolos:
        simbolo = item[0]
        quantidade = item[1]

        massa_atomica = dic_da_tabela_periodica[simbolo][1]

        massa_total += massa_atomica * quantidade

    return massa_total


def main():
    """Executa o programa principal."""

    formula = input("Insira a fórmula molecular da amostra: ")

    massa_da_amostra = float(
        input("Insira a massa em gramas da amostra: ")
    )

    tabela_periodica = criar_tabela_periodica()

    lista_quantidade_simbolos = interpretar_formula(formula)

    massa_molar = calcular_massa_molar(
        lista_quantidade_simbolos,
        tabela_periodica
    )

    numero_mols = massa_da_amostra / massa_molar

    print(f"{massa_molar} gramas/mol")
    print(f"{numero_mols:.5f} mols")


if __name__ == "__main__":
    main()
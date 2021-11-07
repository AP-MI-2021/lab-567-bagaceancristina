from domain.cheltuiala2 import get_tip, get_suma


def get_max_chelt_tip(cheltuieli):
    '''
    determina cea mai mare cheltuiala de la fiecare tip de cheltuieli
    :param cheltuieli: lista cheltuieli
    :return: un dictionar in care cheia este tipul si valoarea
            este suma cu numar maxim al cheltuielii din acel tip
    '''
    result = {}
    for c in cheltuieli:
        tip = get_tip(c)
        suma = get_suma(c)
        if tip not in result:
            result[tip] = c
        else:
            if suma > get_suma(result[tip]):
                result[tip] = c
    return result
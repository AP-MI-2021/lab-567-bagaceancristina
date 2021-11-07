from domain.cheltuiala2 import get_suma, get_numar


def get_sume_per_apartament(cheltuieli):
    '''
     Afișarea sumelor lunare pentru fiecare apartament.
    :param cheltuieli: lista cheltuieli
    :return: un dictionar in care cheia este numarul apartamentului si valorile
            sunt sumele de plata a cheltuielilor acelui apartament
    '''
    result = {}
    for c in cheltuieli:
        ap = get_numar(c)
        suma = get_suma(c)
        if ap not in result:
            result[ap] = suma
        else:
            result[ap] += suma
    return result
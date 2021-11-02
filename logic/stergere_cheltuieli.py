from domain.cheltuiala2 import get_numar, get_id
from logic.crud import delete


def del_chelt_apartament(cheltuieli):
    '''
    sterge cheltuielile unui apartament dat
    :param cheltuieli: lista de cheltuieli
    :return: noua lista de cheltuieli
    '''
    apartament = int(input("Introduceti numarul apartamentului a caror cheltuieli doriti sa le stergeti : "))
    for c in cheltuieli:
        if get_numar(c) == apartament:
            cheltuieli = delete(cheltuieli,get_id(c))
    return cheltuieli
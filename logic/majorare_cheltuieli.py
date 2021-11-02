from domain.cheltuiala2 import get_data, get_suma, creeaza_cheltuiala, get_id, get_numar, get_tip


def majorare(cheltuieli):
    '''
    majoreaza cheltuielile dintr-o anumita data cu o valoare citita
    :param cheltuieli: lista de cheltuieli
    :return: noua lista cu preturi schimbate
    '''
    data = input("Introduceti data in care doriti sa majorati cheltuielile :")
    suma = float(input("Introduceti suma cu care doriti sa majorati cheltuielile :"))
    result_list = []
    for c in cheltuieli:
        if get_data(c) == data:
            pret_nou = get_suma(c) + suma
            result_list.append(creeaza_cheltuiala(get_id(c), get_numar(c), pret_nou, get_data(c),get_tip(c)))
        else :
            result_list.append(c)
    return result_list
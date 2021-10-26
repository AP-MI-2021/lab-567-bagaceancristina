from domain.cheltuiala import creeaza_cheltuiala, get_id


def create(lst_cheltuieli:list, id, nr_ap, suma, data, tip):
    '''
    creeaza o lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param id: id-ul cheltuielii
    :param nr_ap: numar apartament
    :param suma: suma de plata
    :param data: data emiterii cheltuielilor
    :param tip: tipul cheltuielilor
    :return:
    '''
    cheltuiala = creeaza_cheltuiala(id,nr_ap,suma,data,tip)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, id_cheltuiala: int=None):
    '''
    citeste cheltuielile unui apartament
    :param lst_cheltuieli: lista cheltuieli
    :param id_cheltuiala: id-ul  apartamentului
    :return: apartamentum cu id-ul id_cheltuiala sau lista cu toate apartamentele daca id_cheltuiala=None
    '''
    cheltuiala_x = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_x = cheltuiala

    if cheltuiala_x:
        return cheltuiala_x
    return lst_cheltuieli


def delete(lst_cheltuieli, id_cheltuiala):
    '''
    sterge cheltuiala cu id-ul id_cheltuiala
    :param lst_cheltuieli: lista heltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :return:
    '''
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id_cheltuiala:
            new_cheltuieli.append(cheltuiala)
    return new_cheltuieli


def update(lst_cheltuieli, cheltuiala):
    '''
    actualizeaza o prajitura
    :param lst_cheltuieli: lista de prajituri
    :param cheltuiala: prajitura care se va modifica (existenta)
    :return: o lista cu prajitura actualizata
    '''
    new_cheltuieli=[]
    for chelt in lst_cheltuieli:
        if get_id(chelt) != get_id(cheltuiala):
            new_cheltuieli.append(chelt)
        else:
            new_cheltuieli.append(cheltuiala)
    return new_cheltuieli





from domain.cheltuiala2 import creeaza_cheltuiala, get_id


def create(lst_cheltuieli:list, id, nr_ap, suma, data, tip, undo_list:list, redo_list:list):
    """
    creeaza o lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param id: id-ul cheltuielii
    :param nr_ap: numar apartament
    :param suma: suma de plata
    :param data: data emiterii cheltuielilor
    :param tip: tipul cheltuielilor
    :param undo_list: lista pentru undo
    :param redo_list: lista pentru redo
    :return:
    """
    if read(lst_cheltuieli,id) is not None:
        raise ValueError(f'Exista deja o cheltuiala cu id-ul {id}')
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    cheltuiala = creeaza_cheltuiala(id,nr_ap,suma,data,tip)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, id_cheltuiala: int=None):
    """
    citeste cheltuielile unui apartament
    :param lst_cheltuieli: lista cheltuieli
    :param id_cheltuiala: id-ul  apartamentului
    :return: apartamentum cu id-ul id_cheltuiala
            lista cu toate apartamentele daca id_cheltuiala=None
            None daca nu cheltuiala cu ud_cheltuiala
    """
    if not id_cheltuiala:
        return lst_cheltuieli
    cheltuiala_x = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_x = cheltuiala

    if cheltuiala_x:
        return cheltuiala_x
    else:
        return None


def delete(lst_cheltuieli, id_cheltuiala, undo_list:list, redo_list:list):
    """
    sterge cheltuiala cu id-ul id_cheltuiala
    :param lst_cheltuieli: lista heltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :param undo_list: lista pentru undo
    :param redo_list: lista pentru redo
    :return:
    """
    if read(lst_cheltuieli,id_cheltuiala) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {id_cheltuiala} pe care sa o stergem')
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id_cheltuiala:
            new_cheltuieli.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_cheltuieli


def update(lst_cheltuieli, cheltuiala, undo_list:list, redo_list:list):
    """
    actualizeaza o prajitura
    :param lst_cheltuieli: lista de prajituri
    :param cheltuiala: prajitura care se va modifica (existenta)
    :param undo_list: lista pentru undo
    :param redo_list: lista pentru redo
    :return: o lista cu prajitura actualizata
    """
    if read(lst_cheltuieli,get_id(cheltuiala)) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {get_id(cheltuiala)}')
    new_cheltuieli=[]
    for chelt in lst_cheltuieli:
        if get_id(chelt) != get_id(cheltuiala):
            new_cheltuieli.append(chelt)
        else:
            new_cheltuieli.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_cheltuieli





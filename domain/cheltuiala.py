

def creeaza_cheltuiala(id:int, nr_ap:int, suma:float, data, tipul):
    '''
    creeaza o cheltuiala.
    :param id: id cheltuiala unic
    :param nr_ap: Numarul unui apartament, nenul
    :param suma: suma de plata
    :param data: o data din calendar
    :param tipul: tipul cheltuielilor
    :return: o cheltuiala de proprietari
    '''
    return{
        'id': id,
        'nr': nr_ap,
        'suma': suma,
        'data': data,
        'tipul': tipul,
    }


def get_id(cheltuiala):
    '''
    getter-ul pentru id-ul cheltuielii
    :param cheltuiala: cheltuiala
    :return: id-ul cheltuielii date ca parametru
    '''
    return cheltuiala['id']


def get_numar(cheltuiala):
    '''
    getter-ul pentru numarul apartamentului
    :param cheltuiala: cheltuiala
    :return: numarul apartamentului cheltuielii date ca parametru
    '''
    return cheltuiala['nr']


def get_suma(cheltuiala):
    '''
    getter-ul pentru suma de plata
    :param cheltuiala: cheltuiala
    :return: suma de plata a cheltuielii
    '''
    return cheltuiala['suma']


def get_data(cheltuiala):
    '''
    getter-ul de data
    :param cheltuiala: cheltuiala
    :return: data emiterii unei cheltuieli
    '''
    return cheltuiala['data']


def get_tip(cheltuiala):
    '''
    getter-ul tipului de cheltuiala
    :param cheltuiala: cheltuiala
    :return: tipul de cheltuiala
    '''
    return cheltuiala['tipul']


def get_cheltuiala(cheltuiala):
    return f'Cheltuiala cu id-ul {get_id(cheltuiala)}, a apartamentului {get_numar(cheltuiala)}, emisa la data {get_data(cheltuiala)}, in valoare de {get_suma(cheltuiala)}, pentru {get_tip(cheltuiala)}'
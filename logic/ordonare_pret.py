from domain.cheltuiala2 import get_suma
def get_suma_c(cheltuiala):
    return  get_suma(cheltuiala)
def ordonare_suma(cheltuieli):
    '''
    ordoneaza descrescator, cheltuielile in functie de pret
    :param cheltuieli: lista cheltuieli
    :return: lista ordonata
    '''
    return sorted(cheltuieli, key= get_suma, reverse=True)

from domain.cheltuiala2 import creeaza_cheltuiala, get_suma
from logic.majorare_cheltuieli import majorare


def get_data():
    return[
        creeaza_cheltuiala(1, 1, 12.6, '22.12.2002', 'casa'),
        creeaza_cheltuiala(2, 4, 92.6, '22.12.2002', 'gaz'),
        creeaza_cheltuiala(3, 7, 102.8, '02.01.2002', 'apa'),
        creeaza_cheltuiala(4, 9, 77, '19.08.2002', 'lumina')
    ]
def test_majorare():
    cheltuieli = get_data()
    data = "22.12.2002"
    plus = 1.1
    new_cheltuieli =[]
    new_cheltuieli = majorare(cheltuieli,data,plus)
    assert get_suma(cheltuieli[1]) != get_suma(new_cheltuieli[1])
    assert get_suma(cheltuieli[3]) == get_suma(new_cheltuieli[3])
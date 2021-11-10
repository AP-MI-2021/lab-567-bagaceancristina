from domain.cheltuiala2 import creeaza_cheltuiala
from logic.max_cheltuieli_tip import get_max_chelt_tip


def get_data():
    return[
        creeaza_cheltuiala(1, 1, 12.6, '08.12.2012', 'gaz'),
        creeaza_cheltuiala(2, 4, 92.6, '22.12.2002', 'gaz'),
        creeaza_cheltuiala(3, 7, 102.8, '02.01.2002', 'apa'),
        creeaza_cheltuiala(4, 9, 77, '19.08.2002', 'lumina')
    ]


def test_max():
    cheltuieli = get_data()
    result = get_max_chelt_tip(cheltuieli)
    assert len(cheltuieli) != len(result)

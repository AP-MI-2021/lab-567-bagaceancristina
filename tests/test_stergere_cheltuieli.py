from domain.cheltuiala2 import creeaza_cheltuiala
from logic.stergere_cheltuieli import del_chelt_apartament


def get_data():
    return[
        creeaza_cheltuiala(1, 1, 12.6, '08.12.2002', 'casa'),
        creeaza_cheltuiala(2, 1, 92.6, '22.12.2002', 'gaz'),
        creeaza_cheltuiala(3, 7, 102.8, '02.01.2002', 'apa'),
        creeaza_cheltuiala(4, 9, 77, '19.08.2002', 'lumina')
    ]
def test_stergere_cheltuieli():
    cheltuieli = get_data()
    apartament = 1
    new_cheltuieli = del_chelt_apartament(cheltuieli, apartament)
    assert len(cheltuieli) != len(new_cheltuieli)
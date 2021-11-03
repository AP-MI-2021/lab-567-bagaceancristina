from domain.cheltuiala2 import creeaza_cheltuiala, get_id
from logic.crud import create, read, update, delete


def get_data():
    return[
        creeaza_cheltuiala(1, 1, 12.6, '22.12.2002', 'casa'),
        creeaza_cheltuiala(2, 4, 92.6, '12.02.2002', 'gaz'),
        creeaza_cheltuiala(3, 7, 102.8, '02.01.2002', 'apa'),
        creeaza_cheltuiala(4, 9, 77, '19.08.2002', 'lumina')
    ]


def test_create():
    cheltuieli = get_data()
    params = (5, 3, 65, '30.06.2002', 'curent')
    c_new = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params)
    assert len(new_cheltuieli) == len(cheltuieli) + 1

    assert c_new in new_cheltuieli
    params2 = (5, 8, 605, '30.06.2002', 'curent')
    try:
        _ = create(new_cheltuieli, *params2)
        assert False
    except ValueError:
        assert True



def test_read():
    cheltuieli = get_data()
    some_c = cheltuieli[2]
    assert read(cheltuieli, get_id(some_c)) == some_c
    assert read(cheltuieli, None) == cheltuieli


def test_update():
    cheltuieli = get_data()
    c_updated = creeaza_cheltuiala(1, 7, 44, '07.01.2002', 'reparatii')
    updated = update(cheltuieli, c_updated)
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(updated) == len(cheltuieli)


def test_delete():
    cheltuieli = get_data()
    to_delete = 3
    c_deleted = read(cheltuieli, to_delete)
    deleted = delete(cheltuieli, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
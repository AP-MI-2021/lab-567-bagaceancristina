from domain.cheltuiala2 import creeaza_cheltuiala
from logic.crud import delete
from logic.undo_redo import do_undo, do_redo


def get_data():
    return[
        creeaza_cheltuiala(1, 1, 12.6, '08.12.2012', 'gaz'),
        creeaza_cheltuiala(2, 4, 92.6, '22.12.2002', 'gaz'),
        creeaza_cheltuiala(3, 7, 102.8, '02.01.2002', 'apa'),
        creeaza_cheltuiala(4, 9, 77, '19.08.2002', 'lumina')
    ]


def test_undo():
    cheltuieli1 = get_data()
    cheltuieli2 = get_data()
    undo_list = []
    redo_list = []
    delete(cheltuieli1, 1, undo_list, redo_list)
    cheltuieli1 = do_undo(undo_list, redo_list, cheltuieli1)
    assert cheltuieli1 == cheltuieli2


def test_redo():
    cheltuieli1 = get_data()
    cheltuieli2 = get_data()
    undo_list = []
    redo_list = []
    id = 1
    cheltuieli1 = delete(cheltuieli1, id, undo_list, redo_list)
    cheltuieli1 = do_undo(undo_list, redo_list, cheltuieli1)
    cheltuieli1 = do_redo(undo_list, redo_list, cheltuieli1)
    cheltuieli2 = delete(cheltuieli2, id, undo_list, redo_list)
    assert cheltuieli1 == cheltuieli2


def test_undo_redo():
    test_undo()
    test_redo()

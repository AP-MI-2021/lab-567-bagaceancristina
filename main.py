from UserInterface.console import run_ui
from UserInterface.console2 import console2
from logic.crud import create
from tests.test_crud import test_crud
from tests.test_majorare import test_majorare
from tests.test_max_chelt_tip import test_max
from tests.test_stergere_cheltuieli import test_stergere_cheltuieli
from tests.test_undo_redo import test_undo_redo


def main():
    cheltuieli = []
    undo_list = []
    redo_list = []
    cheltuieli = create(cheltuieli, 1, 1, 100, "11.12.2002", "gaz", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 2, 1, 60, "10.02.2002", "curent", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 3, 2, 110, "14.10.2002", "gaz", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 4, 3, 45.12, "18.08.2001", "apa", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 5, 4, 244.8, "11.12.2002", "gaz", undo_list, redo_list)
    cheltuieli = run_ui(cheltuieli, undo_list, redo_list)
    #cheltuieli = console2(cheltuieli)


if __name__ == '__main__':
    test_crud()
    test_majorare()
    test_stergere_cheltuieli()
    test_max()
    test_undo_redo()
    main()
    #console2()


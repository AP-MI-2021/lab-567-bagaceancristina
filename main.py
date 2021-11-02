from UserInterface.console import run_ui
from tests.test_crud import test_crud
from tests.test_majorare import test_majorare
from tests.test_stergere_cheltuieli import test_stergere_cheltuieli


def main():
    cheltuieli = []
    cheltuieli = run_ui(cheltuieli)

if __name__ == '__main__':
    test_crud()
    test_majorare()
    test_stergere_cheltuieli()
    main()


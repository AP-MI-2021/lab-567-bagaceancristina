from UserInterface.console import run_ui
from tests.test_crud import test_crud

def main():
    cheltuieli = []
    cheltuieli = run_ui(cheltuieli)
if __name__ == '__main__':
    test_crud()
    main()


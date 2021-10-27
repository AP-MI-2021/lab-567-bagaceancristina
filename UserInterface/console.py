from domain.cheltuiala2 import get_cheltuiala
from logic.crud import create


def show_menu():
    print('1.CRUD')
    print('2.restu')
    print('x.Exit')

def handle_add(cheltuieli):
    id = int (input('Dati id-ul cheltuielii: '))
    nr_ap = int (input('Dati numarul apartamentului: '))
    suma = float (input('Dati suma cheltuielii: '))
    data = input('Dati data emiterii cheltuielii: ')
    tipul = input('Dati tipul cheltuielii: ')
    return create(cheltuieli, id, nr_ap, suma, data, tipul)


def handle_show_all(cheltuieli):
    for c in cheltuieli:
        print(get_cheltuiala(c))


def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa :')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return cheltuieli

def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == 'x':
            break
        else :
            print('Optiune invaida')

    return cheltuieli
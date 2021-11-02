from domain.cheltuiala2 import get_cheltuiala
from logic.crud import create, update, delete
from logic.majorare_cheltuieli import majorare
from logic.stergere_cheltuieli import del_chelt_apartament


def show_menu():
    print('1.CRUD')
    print('2.Stergerea cheltuielilor unui apartament dat.')
    print('3.Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
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

def handle_update(cheltuieli):
    id = int(input('Dati id-ul cheltuielii care se modifica: '))
    nr_ap = int(input('Dati noul numarul apartamentului: '))
    suma = float(input('Dati noua suma cheltuielii: '))
    data = input('Dati noua data de emiterie a cheltuielii: ')
    tipul = input('Dati noul tip de cheltuiala: ')
    return update(cheltuieli, id, nr_ap, suma, data, tipul)


def handle_delete(cheltuieli):
    id = int(input('Dati id-ul cheltuielii care se va sterge: '))
    return delete(cheltuieli, id)

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
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli)
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
        elif optiune == '2':
            apartament = int(input("Introduceti numarul apartamentului a caror cheltuieli doriti sa le stergeti : "))
            cheltuieli = del_chelt_apartament(cheltuieli, apartament)
        elif optiune == '3':
            data = input("Introduceti data in care doriti sa majorati cheltuielile :")
            suma = float(input("Introduceti suma cu care doriti sa majorati cheltuielile :"))
            cheltuieli = majorare(cheltuieli, data, suma)
        elif optiune == 'x':
            break
        else :
            print('Optiune invaida')

    return cheltuieli
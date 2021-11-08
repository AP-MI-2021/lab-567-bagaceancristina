from domain.cheltuiala2 import get_cheltuiala
from logic.crud import create, update, delete
from logic.majorare_cheltuieli import majorare
from logic.max_cheltuieli_tip import get_max_chelt_tip
from logic.ordonare_pret import ordonare_suma
from logic.stergere_cheltuieli import del_chelt_apartament
from logic.sume_pt_fiecare_ap import get_sume_per_apartament
from logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1.CRUD')
    print('2.Stergerea cheltuielilor unui apartament dat.')
    print('3.Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('4.Afisarea celei mai scumpe cheltuieli pentru fiecare tip de cheltuiala.')
    print('5.Ordonarea cheltuielilor in functie de suma.')
    print('6.Afișarea sumelor lunare pentru fiecare apartament.')
    print('u.Undo.')
    print('r.Redo.')
    print('x.Exit')


def handle_add(cheltuieli, undo_list, redo_list):
    try:
        id = int (input('Dati id-ul cheltuielii: '))
        nr_ap = int (input('Dati numarul apartamentului: '))
        suma = float (input('Dati suma cheltuielii: '))
        data = input('Dati data emiterii cheltuielii: ')
        tipul = input('Dati tipul cheltuielii: ')
        return create(cheltuieli, id, nr_ap, suma, data, tipul, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli


def handle_show_all(cheltuieli):
    for c in cheltuieli:
        print(get_cheltuiala(c))


def handle_update(cheltuieli, undo_list, redo_list):
    try:
        id = int(input('Dati id-ul cheltuielii care se modifica: '))
        nr_ap = int(input('Dati noul numarul apartamentului: '))
        suma = float(input('Dati noua suma cheltuielii: '))
        data = input('Dati noua data de emiterie a cheltuielii: ')
        tipul = input('Dati noul tip de cheltuiala: ')
        return update(cheltuieli, id, nr_ap, suma, data, tipul, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare', ve)
    return cheltuieli


def handle_delete(cheltuieli, undo_list, redo_list):
    try:
        id = int(input('Dati id-ul cheltuielii care se va sterge: '))
        return delete(cheltuieli, id, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare', ve)
    return cheltuieli


def handle_del_chelt_ap(cheltuieli, undo_list, redo_list):
    try:
        apartament = int(input("Introduceti numarul apartamentului a caror cheltuieli doriti sa le stergeti : "))
        result = del_chelt_apartament(cheltuieli, apartament, undo_list, redo_list)
        print('Stergerea a fost efectuata.')
        print(result)
        return result
    except ValueError as ve:
        print('Eroare: ', ve)
    return cheltuieli


def handle_majorare(cheltuieli):
    try:
        data = input("Introduceti data in care doriti sa majorati cheltuielile :")
        suma = float(input("Introduceti suma cu care doriti sa majorati cheltuielile :"))
        result = majorare(cheltuieli, data, suma)
        print('Majorarea a fost efectuata.')
        print(result)
        return result
    except ValueError as ve:
        print('Eroare : ', ve)
    return cheltuieli


def handle_max_chelt_tip(cheltuieli):
    result = get_max_chelt_tip(cheltuieli)
    print(result)


def handle_ordonare(cheltuieli):
    result = ordonare_suma(cheltuieli)
    handle_show_all(result)


def handle_sume_pt_fiecare_ap(cheltuieli):
    result = get_sume_per_apartament(cheltuieli)
    print(result)


def handle_undo(cheltuieli, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list)
    if undo_result is not None:
        return undo_result
    return cheltuieli


def handle_redo(cheltuieli, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list)
    if redo_result is not None:
        return redo_result
    return cheltuieli


def handle_crud(cheltuieli, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa :')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return cheltuieli


def run_ui(cheltuieli, undo_list, redo_list):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = handle_del_chelt_ap(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = handle_majorare(cheltuieli)
        elif optiune == '4':
            handle_max_chelt_tip(cheltuieli)
        elif optiune == '5':
            handle_ordonare(cheltuieli)
        elif optiune == '6':
            handle_sume_pt_fiecare_ap(cheltuieli)
        elif optiune == 'u':
            cheltuieli = handle_undo(cheltuieli, undo_list, redo_list)
        elif optiune == 'r':
            cheltuieli = handle_redo(cheltuieli, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invaida')

    return cheltuieli
from domain.cheltuiala2 import creeaza_cheltuiala, get_cheltuiala
from logic.crud import read, delete, update, create


def handle_showall(lst_cheltuieli):
    for c in lst_cheltuieli:
        print(get_cheltuiala(c))


def handle_modificare(lst_cheltuiala_modificata, lst_cheltuieli):
        try:
            id_cheltuiala = int(lst_cheltuiala_modificata[1])
            nr_apartament = int(lst_cheltuiala_modificata[2])
            suma = float(lst_cheltuiala_modificata[3])
            data = lst_cheltuiala_modificata[4]
            tipul =lst_cheltuiala_modificata[5]
            new_c = creeaza_cheltuiala(id_cheltuiala,nr_apartament,suma,data,tipul)
            lst_cheltuieli = update(lst_cheltuieli,new_c)
        except ValueError as ve:
            print('Nu ati introdus o valoare valida', ve)
        return lst_cheltuieli


def handle_adaugare(lst_cheltuiala_noua, lst_cheltuieli):
    try:
        id_cheltuiala = int(lst_cheltuiala_noua[1])
        nr_apartament = int(lst_cheltuiala_noua[2])
        suma = float(lst_cheltuiala_noua[3])
        data = lst_cheltuiala_noua[4]
        tipul =lst_cheltuiala_noua[5]
        return create(lst_cheltuieli,id_cheltuiala,nr_apartament,suma,data,tipul)
    except ValueError as ve:
        print('Nu ati introdus o valoare valida',ve)
    return lst_cheltuieli


def handle_stergere(lst_cheltuiala_stearsa, lst_cheltuieli):
    try:
        id = int(lst_cheltuiala_stearsa[1])
        if read(lst_cheltuieli,id) is None:
            raise ValueError('Cheltuiala cu id-ul introdus nu exista')
        lst_cheltuieli = delete(lst_cheltuieli, id)
    except ValueError as ve:
        print('Eroare, nu ati introdus o valoare valida pentru id',ve)
    return lst_cheltuieli


def show_menu():
    print(
        """
        Meniu:
        Adauga cheltuiala -add- :id_cheltuiala, nr_apartament, suma, data, tipul
        Stergere cheltuiala -delete- :id_cheltuiala
        Modificare cheltuiala -update- :id_cheltuiala, nr_apartament, suma, data, tipul
        Afisare cheltuieli -showall-
        Iesire -exit-
        """)

def console2():
    lst_cheltuieli = []
    done = False
    try:
        while not done:
            show_menu()
            comenzi = input("Introduceti comenzile separate prin ';', iar detaliitle pentru fiecare comanda prin ',': ")
            comenzi = comenzi.split(";")

            for comanda in comenzi:
                comanda = comanda.split(",")
                lst_cheltuieli_comanda = []
                for detalii in comanda:
                    lst_cheltuieli_comanda.append(detalii)
                if lst_cheltuieli_comanda[0] == "add":
                    lst_cheltuieli = handle_adaugare(lst_cheltuieli_comanda,lst_cheltuieli)
                elif lst_cheltuieli_comanda[0] == "delete":
                    lst_cheltuieli = handle_stergere(lst_cheltuieli_comanda,lst_cheltuieli)
                elif lst_cheltuieli_comanda[0] == "update":
                    lst_cheltuieli = handle_modificare(lst_cheltuieli_comanda,lst_cheltuieli)
                elif lst_cheltuieli_comanda[0] == "showall":
                    handle_showall(lst_cheltuieli)
                elif lst_cheltuieli_comanda[0] == "exit":
                    done = True
                else:
                    print('Nu ati introdus o comanda valida')
    except ValueError as ve:
        print("Eroare", ve)



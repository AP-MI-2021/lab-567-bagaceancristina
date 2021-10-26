from domain.cheltuiala import creeaza_cheltuiala, get_cheltuiala
from logic.crud import create, read, delete, update

cheltuieli_bloc =[]
cheltuiala = creeaza_cheltuiala(2,1,66.7,9,'gaz')
print(get_cheltuiala(cheltuiala))
cheltuieli_bloc = create(cheltuieli_bloc,2,2,78,9,'curent')
cheltuieli_bloc = create(cheltuieli_bloc,3,2,30,9,'gaz')
cheltuieli_bloc = create(cheltuieli_bloc,4,3,99.8,9,'curent')
print(read(cheltuieli_bloc,None))
cheltuieli_bloc = delete(cheltuieli_bloc,3)
print(read(cheltuieli_bloc,None))
cheltuieli_bloc = update(cheltuieli_bloc,cheltuiala)
print(read(cheltuieli_bloc,None))
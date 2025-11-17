# kolekcje - przechowuje wiele elementów, róznego typu na raz

# lista - zachowuje kolejnosć przy dodawaniu elemntów
lista = []  # pusta lista
lista_pusta = list()  # []
print(lista)  # []
print(type(lista))  # <class 'list'>

lista_pusta.append("Piotr")
lista_pusta.append("Radek")
lista_pusta.append("Tomek")
lista_pusta.append("Zenek")
lista_pusta.append("Aga")
print(lista_pusta)  # ['Piotr', 'Radek', 'Tomek', 'Zenek', 'Aga']

lista_pusta.sort()
print(lista_pusta)  # ['Aga', 'Piotr', 'Radek', 'Tomek', 'Zenek'], zmienił oryginal

lista_pusta.append(345)
print(lista_pusta)  # ['Aga', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]
# lista_pusta.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'

# indeksowanie od 0
# wstawienie eleemntu na konkretny indeks
lista_pusta.insert(1, "Magda")
print(lista_pusta)  # ['Aga', 'Magda', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]

print(lista_pusta[0])  # Aga
# print(lista_pusta[23])  # IndexError: list index out of range

# ostatni element
print(lista_pusta[len(lista_pusta) - 1])  # 345
print(lista_pusta[-1])  # 345

print(lista_pusta[-2])  # Zenek

# slicowanie - fragment listy
#  ['Aga', 'Magda', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]
print(lista_pusta[0:2])  # ['Aga', 'Magda'] z prawej otwarty
print(lista_pusta[:2])  # ['Aga', 'Magda']
print(lista_pusta[1:])  # ['Magda', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345], włacznie z ostatnim
print(lista_pusta[1:-1])  # ['Magda', 'Piotr', 'Radek', 'Tomek', 'Zenek'] - ostatni niewłacznie
print(lista_pusta[0:4:2])  # ['Aga', 'Piotr']
# [start:stop:krok]

print(lista_pusta[::-1])
# [345, 'Zenek', 'Tomek', 'Radek', 'Piotr', 'Magda', 'Aga']

print(lista_pusta[45:90])  # []

# usunięcie elementu
lista_pusta.remove("Magda")  # usunie pierwszą od lewej
print(lista_pusta)  # ['Aga', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]

osoby = ['Tomek', 'Ewa', "Adam"]
osoby.extend(lista_pusta)
print(osoby)  # ['Tomek', 'Ewa', 'Adam', 'Aga', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]

a = 1
b = 2
a = b
print(f"{a=}, {b=}")  # a=2, b=2
b = 3
print(f"{a=}, {b=}")  # a=2, b=3

nowa_lista = lista_pusta  # kopia referesncji, adresu
lista_copy = lista_pusta.copy()
print(lista_pusta)  # ['Aga', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]
print(nowa_lista)  # ['Aga', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]
lista_pusta.clear()  # usunięcie wszystkich elementów z listy
print(lista_pusta)  # []
print(lista_copy)  # ['Aga', 'Piotr', 'Radek', 'Tomek', 'Zenek', 345]
print(id(lista_copy))  # 1804423946112
print(id(nowa_lista))  # 1804424478016
print(id(lista_pusta))  # 1804424478016

# krotka - tuple - lista tylko do odczytu
# pozwala lepiej zarządzac pamięcią
krotka = (23, 34, 56, 'Radek')
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (23, 34, 56, 'Radek')

krotka1 = "radek", "tomek", "zenek"
print(type(krotka1))
print(krotka1)  # ('radek', 'tomek', 'zenek')

krotka2 = ("Radek",)
print(krotka2)  # ('Radek',)

# rozpakowanie krotki
print(len(krotka))  # długośc 4
# a,b,c,d
# (23, 34, 56, 'Radek')
a = krotka[0]
a, b, c, d = krotka
a, b, c, d = (23, 34, 56, 'Radek')  # przypisanie kolejnych wartosci do kolejnych zmiennych
print(a, b, c, d)  # 23 34 56 Radek
a, b, *c = (23, 34, 56, 'Radek')  # * pozostałe elementy (worek na dane)
print(a, b, c)  # 23 34 [56, 'Radek']

a, *b, c = (23, 34, 56, 'Radek')
print(a, b, c)  # 23 [34, 56] Radek

# nie ma możliwości zmiany krotki
# krotka[0] = 4  # TypeError: 'tuple' object does not support item assignment

# słownik - dane typu klucz-wartosc
# odpowiednik jsona
oceny = {
    "Tomek": 4,
    "Radek": 5,
    "agata": 5,
    "Zenek": 6,
}

print(oceny)  # {'Tomek': 4, 'Radek': 5, 'agata': 5, 'Zenek': 6}
print(type(oceny))  # <class 'dict'>
print(oceny['Tomek'])  # 4
# print(oceny['tomek'])  # KeyError: 'tomek'
print(oceny.get("Tomek"))  # 4
print(oceny.get("tomek", "default"))  # default

print(oceny.keys())
print(oceny.values())
print(oceny.items())
# dict_keys(['Tomek', 'Radek', 'agata', 'Zenek'])
# dict_values([4, 5, 5, 6])
# dict_items([('Tomek', 4), ('Radek', 5), ('agata', 5), ('Zenek', 6)])

oceny['agata'] = 6
print(oceny)  # {'Tomek': 4, 'Radek': 5, 'agata': 6, 'Zenek': 6}

lista_oceny = [3, 4, 5, 6, 5, 5]
oceny['Tomek'] = lista_oceny
print(oceny)
# {'Tomek': [3, 4, 5, 6, 5, 5], 'Radek': 5, 'agata': 6, 'Zenek': 6}
print(oceny['Tomek'][2])  # 5

dictionary = {}
dict_pusty = dict()
print(type(dictionary))  # <class 'dict'>
print(type(dict_pusty))  # <class 'dict'>
print(dict_pusty)  # {}

# zbior - set()
# przechowuje unikalne wartosci
# nie zachowuje kolejności przy dodawaniu elemntów
# nie posiada indeksu
lista = [45, 55, 66, 77, 45, 55]
zbior1 = set(lista)
print(zbior1)  # {66, 77, 45, 55}

pusty_zbior = set()
print(pusty_zbior)  # set()
print(type(pusty_zbior))  # <class 'set'>

zbior1.add(100)
zbior1.add(102)
zbior1.add(105)
zbior1.add(77)
zbior1.add(55)
print(zbior1)  # {66, 100, 102, 105, 77, 45, 55}

zbior2 = {45, 55, 166, 177}

# część wspolna
print(zbior1.intersection(zbior2))  # {45, 55}
print(zbior1 & zbior2)  # {45, 55}

# róznica
print(zbior2.difference(zbior1))
print(zbior2 - zbior1)  # {177, 166}

lista_ze_zbioru = list(zbior1)
print(lista_ze_zbioru)  # [66, 100, 102, 105, 77, 45, 55]

matrix = [[3, 4, 5], [6, 7], [8, 9, 0]]
print(matrix)  # [[3, 4, 5], [6, 7], [8, 9, 0]]
print(matrix[0][0])  # 3

imie = input("Podaj imię:")
print(imie)
# Podaj imię:Radek
# Radek

# input zwraca str
a = input("Podaj liczbę a:")
print(type(a))
b = input("Podaj liczbę b:")
print(type(b))
print(int(a) + float(b))
# Podaj imię:radek
# radek
# Podaj liczbę a:1
# <class 'str'>
# Podaj liczbę b:2
# <class 'str'>
# 3.0

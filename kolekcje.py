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


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

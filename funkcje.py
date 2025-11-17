# funkcje - wydzielony fragment kodu, można go wywołąc w dowolnym momencie
# może przyjmowąc argumenty

# deklaracja funkcji
# nie zwraca wyniku
def witaj():
    print("Witaj!!")


# wykonanie funkcji
witaj()  # Witaj!!


# funkcje zwracające wynik
def ksero(tekst: str, ile: int):
    """
    Ta funkcja zwraca string pomnożony zadaną ilośc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile  # zwraca wynik (return)


print(ksero("Radek", 5))


# RadekRadekRadekRadekRadek

def ksero2(tekst: str, ile=1):  # argumenty z wartoscią domyślną
    """
    Ta funkcja zwraca string pomnożony zadaną ilośc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile  # zwraca wynik (return)


print(ksero2("Radek"))  # Radek
print(ksero2("Radek", 3))  # RadekRadekRadek


def ile_razy(*ile, **co):
    print(ile)  # (4, 5, 6)
    print(co)


# * argumenty pozycyjne
# ** argumenty nazwane, słownikowe
ile_razy(4, 5, 6)  # (4, 5, 6) -> ile
ile_razy(a=10, b=67, c=90)  # {'a': 10, 'b': 67, 'c': 90} -> co
ile_razy(4, 5, 6, a=10, b=45, c=90)
# (4, 5, 6)
# {'a': 10, 'b': 45, 'c': 90}

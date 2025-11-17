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


print("Radek")  # Radek
print("Radek", 3)  # Radek 3

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


def multi(a, b):
    try:
        return a * b
    except TypeError:
        return "Nieprawidłowe dane"
    except ValueError:
        return 0


print(multi(4, 4))  # 16
print(multi("4", 4))  # 4444
print(multi(4, None))  # Nieprawidłowe dane


def multi2(a, b):
    try:
        return a * b
    except Exception as e:
        return "nieprawidłowe dane:", e.args


print(multi2(4, 4))  #
print(multi2("4", 4))
print(multi2(4, None))  # ('nieprawidłowe dane:', ("unsupported operand type(s) for *: 'int' and 'NoneType'",))

try:
    print(5 / 0)
except ZeroDivisionError:
    print("Nie dziel przez zero")
# Nie dziel przez zero

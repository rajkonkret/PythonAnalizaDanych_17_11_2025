# https://kariera.comarch.pl/blog/clean-code-15-krokow-do-stworzenia-czystego-kodu/
# https://peps.python.org/pep-0008/
import sys

# snake_case

# inline completion -> settings
print("Hello World")
print("Hello World")
print()

print('Hello')

# ctrl / - komentarz
# print("Radek')
#   File "C:\Users\CSComarch\PycharmProjects\PythonAnalizaDanych_17_11_2025\pierwszy.py", line 13
#     print("Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 13)
#
# Process finished with exit code 1

# typy danych
# type()
print(type("Radek"))  # <class 'str'>

print("39" + "90")  # 3990, konkatenacja, łaczenie tekstów

# print("39" + 14) # TypeError: can only concatenate str (not "int") to str
# silne typownie - nie zamienia typów sam

# ctrl alt l - formtowanie pep8
print(type(39))  # <class 'int'>, liczba calkowita
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# zmienna - pudełko na dane

# typowanie dynamiczne, typ jesy wnioskowany na podstawie danych
name = "Radek"
print(type(name))  # <class 'str'>

name = 90
print(type(name))  # <class 'int'>

# podpowiedzi typów
name: str = "radek"
print(name)
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90

# mypy - sprawdza poprawnosc typów
# pip - instalator pakietów
#  pip install mypy
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonAnalizaDanych_17_11_2025> mypy .\pierwszy.py
# pierwszy.py:44: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:48: error: Name "name" already defined on line 41  [no-redef]
# pierwszy.py:52: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonAnalizaDanych_17_11_2025>

# teksty są niemutowalne
tekst = "Witaj Świecie"
tekst.upper()
print(tekst)  # Witaj Świecie, nie uległo zmianie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
zmienna = tekst.upper()
print(zmienna)

# ctrl d - powielenie lini
print(zmienna.lower())  # witaj świecie
print(zmienna.capitalize())  # Witaj świecie

zmienna1 = "GROSS"
zmienna2 = "groẞ"

# == porównanie
print(zmienna1.lower() == zmienna2.lower())  # False
print(zmienna1.casefold() == zmienna2.casefold())  # True - wg zasad unicode

# != rózne
print(1 != 8)  # True

# rzutowanie - zamiana typów
print(int("39"))  # rzytowanie na int
print(str(39))  # rzutowanie na str
print(168 * "35")
print(168 * 35)  # 5880
print(10 * "-")  # ----------
print(int(168) * int("35"))  # 5880

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool("radek"))  # True

print(bool(""))  # False

# None - odpowiednik null, nie wiem, stan nieokreslony
print(bool(None))  # False

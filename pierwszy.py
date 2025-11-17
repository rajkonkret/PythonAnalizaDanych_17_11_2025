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

temp = 36.6
print(type(temp))  # <class 'float'>
print(temp)  # 36.6
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
# min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal - ominięcie problemu zaokrąglenia

# f - string format
name = "Radek"
print(f"Nazywam się {name}")  # Nazywam się Radek
print("Nazywam się {}.".format(name))  # Nazywam się Radek.

liczba = 3.900001
print(f"Wersja pythona: {liczba}")  # Wersja pythona: 3.900001
print(f"Wersja pythona: {liczba:.2f}")  # Wersja pythona: 3.90

print(f"""Teskt
    wielolinijkowy""")
# "Teskt
#     wielolinijkowy"

"""Komentarz
wielolinijowy.
Komentarz dokumentacyjny"""
print(print.__doc__)  # dokumentacja

starszy = 'Mam na imię %s'
# %s - str
print(starszy % name)  # Mam na imię Radek

print("Wynik:", liczba)  # Wynik: 3.900001
#   sep
#         string inserted between values, default a space.
print("wynik:", liczba, sep="....")  # wynik:....3.900001

print(100 / 3)  # 33.333333333333336
print(100 // 3)  # 33
print(100 % 3)  # modulo, reszta z dzielenia, 1

zysk = 8901234567654
print(f'Nasza duza liczba: {zysk}')
print(f'Nasza duza liczba: {zysk:,}')  # Nasza duza liczba: 8,901,234,567,654
print(f'Nasza duza liczba: {zysk:_}')  # Nasza duza liczba: 8_901_234_567_654
print(f'Nasza duza liczba: {zysk:_}'.replace("_", " "))  # Nasza duza liczba: 8 901 234 567 654

paramter = 1_000_000_000
print(paramter)  # 1000000000
print(type(paramter))  # <class 'int'>

encoded_text = tekst.encode("utf-8")
print(encoded_text)  # b'Witaj \xc5\x9awiecie'
# \xc5\x9a - kod litery Ś w sytemie szesnastkowym -> \x
print(type(encoded_text))  # <class 'bytes'>
print(encoded_text.decode("utf-8"))  # Witaj Świecie

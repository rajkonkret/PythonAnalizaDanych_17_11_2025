# liczba = int(input("Podaj liczbę"))
#
# if liczba < 4:
#     print("Przegrałeś")
# elif liczba > 5:
#     print("Spróbuj ponownie")
# elif liczba == 5:
#     print("wygrałeś")
# else:  # w innym przypadku
#     print("Nieznany bład")
# # Podaj liczbę5
# # wygrałeś

# od python 3.10

lang = input("Podaj znany Ci język programowania")

match lang.casefold().strip():  # strip() - czyszczenie białych znaków
    case "python":
        print("Znam Pythona")
    case "java":
        print("Możesz zostać backend developerem")
    case "c++":
        print("Możesz pisać gry")
    case _:  # odpowiednik else
        print("Inny przypadek")

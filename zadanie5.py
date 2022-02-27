#try:
#   -instrukcje które mogą zawierać błąd
#except nazwa_bledu:
#   -instrukcje gdy blad nastapi
#except nastepna_nazwa_bledu:
#   -instrukcje
#else:
#   -instrukcje
#nie jest konieczny

a = input("podaj pierwszą liczbę: ")
b = input("podaj drugą liczbę: ")

try:
    a = int(a)
    b = int(b)
    wynik = a/b
    print(wynik)
except ZeroDivisionError:
    print("dzielisz przez zero!")
except ValueError:
    print("to nie jest liczba")
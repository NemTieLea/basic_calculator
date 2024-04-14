# Wartosci stale
SZABLON_POWITANIA = """Witaj, {}! Jestem kalkulatorem, w tej wersji potrafie tylko dodawac.
Podaj dwie liczby, a ja podam ich sume."""

SZABLON_WYNIKU = "Suma liczb {} i {} to: {}"



# Przetwarzanie danych

imie = input("Podaj swoje imie: ")

print(SZABLON_POWITANIA.format(imie))

liczba_1 = float(input("Liczba 1: "))
liczba_2 = float(input("Liczba 2: "))

suma = liczba_1 + liczba_2

print(SZABLON_WYNIKU.format(liczba_1, liczba_2, suma))

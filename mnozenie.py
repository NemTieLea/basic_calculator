# Wartosci stale

SZABLON_POWITANIA = """Witaj, {}! Jestem kalkulatorem, w tej wersji potrafie tylko mnozyc.
Podaj dwie liczby, a ja podam ich iloczyn."""

# Przetwarzanie danych

imie = input("Podaj swoje imie: ")

print(SZABLON_POWITANIA.format(imie))

czynnik_1 = float(input("Czynnik 1: "))
czynnik_2 = float(input("Czynnik 2: "))

iloczyn = czynnik_1 * czynnik_2

print(f"Iloczyn liczb {czynnik_1} i {czynnik_2} to {iloczyn}")

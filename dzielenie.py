# Wartosci stale

SZABLON_POWITANIA = """Witaj, {}! Jestem kalkulatorem, w tej wersji potrafie tylko dzielic.
Podaj dwie liczby, a ja podam ich iloraz.
!!! DZIELNIK MUSI BYC WIEKSZY OD ZERA !!!"""

# Przetwarzanie danych

imie = input("Podaj swoje imie: ")

print(SZABLON_POWITANIA.format(imie))

dzielna = float(input("Podaj dzielna: "))
dzielnik = float(input("Podaj dzielnik: "))

iloraz = dzielna / dzielnik

print(f"Wynik dzielenia {dzielna} przez {dzielnik} to: {iloraz}")

# Wartosci stale
SZABLON_POWITANIA = """Witaj, {}! Jestem kalkulatorem, w tej wersji potrafie tylko dodawac.
Podaj dwie liczby, a ja podam ich sume."""

# Przetwarzanie danych

imie = input("Podaj swoje imie: ")

print(SZABLON_POWITANIA.format(imie))

liczba_1 = float(input("Liczba 1: "))
liczba_2 = float(input("Liczba 2: "))

suma = liczba_1 + liczba_2

print(f"Suma liczb {liczba_1} i {liczba_2} to: {suma}")

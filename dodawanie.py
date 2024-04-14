# Wartosci stale

SZABLON_POWITANIA = """Witaj, {}! Jestem kalkulatorem, w tej wersji potrafie tylko dodawac.
Podaj dwie liczby, a ja podam ich sume.
Na koniec powiem tez, czy suma jest wieksza od 0."""

# Przetwarzanie danych

imie = input("Podaj swoje imie: ")

print(SZABLON_POWITANIA.format(imie))

liczba_1 = float(input("Liczba 1: "))
liczba_2 = float(input("Liczba 2: "))

suma = liczba_1 + liczba_2
suma_wieksza_od_0 = suma > 0

print(f"Suma liczb {liczba_1} i {liczba_2} to: {suma}")
print(f"Suma wieksza od zera: {suma_wieksza_od_0}")

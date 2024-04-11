imie = input("Podaj swoje imie: ")

szablon_powitania = """Witaj, {}! Jestem kalkulatorem, w tej wersji potrafie tylko dodawac.
Podaj dwie liczby, a ja podam ich sume. Podawaj tylko liczby calkowite"""

print(szablon_powitania.format(imie))

liczba_1 = int(input("Liczba 1: "))
liczba_2 = int(input("Liczba 2: "))

suma = liczba_1 + liczba_2

szablon_wyniku = "Suma liczb {} i {} to: {}"

print(szablon_wyniku.format(liczba_1, liczba_2, suma))

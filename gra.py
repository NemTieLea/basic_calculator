# Wartosci stale
separator = "="*30 + "||" + "="*30

# Generowanie liczby do zgadniecia
LICZBA_DO_ZGADYWANIA = 52

# Przywitanie i zasady
print(separator)
print("Gra polega na zgadywaniu liczb. Liczba miesci sie miedzy 1 a 100.")
print("program powie czy podana liczba jest wieksza czy wieksza niz proba")
print(separator)

# Pobieranie liczby od usera
proba = int(input("Podaj liczbe: "))
print(separator)

# Sprawdzanie podpowiedzi i warunku wygrania
liczba_za_mala = proba < LICZBA_DO_ZGADYWANIA
wygrana = proba == LICZBA_DO_ZGADYWANIA

# Wyswietlanie wyniku
print(f"Liczba jest za mala: {liczba_za_mala}")
print(f"Podano dobra liczbe: {wygrana}")
print(separator)

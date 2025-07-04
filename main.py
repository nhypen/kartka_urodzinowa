from datetime import datetime

# pobieranie danych od użytkownika
imie_odbiorcy = input("Podaj imię odbiorcy: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiadomosc = input("Wpisz spersonalizowaną wiadomość: ")
imie_nadawcy = input("Podaj swoje imie (nadawcy): ")

# Obliczanie wieku
obecny_rok = datetime.now().year
wiek = obecny_rok - rok_urodzenia

# generowanie kartki urodzinowej
print("\n--- Kartka Urodzinowa ---")
print(f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek} urodzin!")
print(wiadomosc)
print(f"{imie_nadawcy}")

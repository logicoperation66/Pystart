"""Zadanie 5
Przygotuj program, który na podstawie wieku urodzenia danej osoby, odpowie ile ta osoba
ma lat, czy jest pełnoletnia oraz czy rok w którym się urodziła był rokiem przestępnym.
Zwróć uwagę, że taki rok nie zawsze przypada co cztery lata :) Rok bieżący możesz
przechowywać w jednej zmiennej zadeklarowanej na początku programu.
"""



curent_year = 2021

birth_year = int(input("Podaj w którym roku się urodziłeś. "))

print(f"Masz {curent_year-birth_year} lat")

if birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0):
    print(f"Rok {birth_year} jest przestępny")
else:
    print(f"Rok {birth_year} Jest nieprzestępny.")

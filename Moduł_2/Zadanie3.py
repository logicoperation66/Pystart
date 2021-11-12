"""Zapytaj użytkownika o 10 liczb dodatnich. Jeśli użytkownik
poda liczbę ujemną to nie powinna być ona zliczana. Wyświetl
największą i najmniejszą liczbę."""


numbers = []

while len(numbers) < 10:
    number = int(input("Podaj liczbę:"))
    if number not in numbers:
        if number > 0:
            numbers.append(number)
        elif number < 0:
            print("Podaj liczbę dodatnią")
    else:
        print("Ta liczba już znajduje się na liście")

print(numbers)
print(f"Najmniejszą liczbą na liście jest: {min(numbers)}")
print(f"Najwiekszą liczbą na liście jest: {max(numbers)}")
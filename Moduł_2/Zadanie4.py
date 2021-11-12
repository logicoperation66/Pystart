"""Poproś użytkownika o podawanie liczb, gdzie każda kolejna
będzie większa od poprzedniej. Jeśli ten warunek nie nastąpi.
Program powinien się zakończyć. Wyświetl średnią z tych
liczb."""

active = True
number = int(input("Podaj liczbę"))
numbers = [number]
while active:
    number2 = int(input("Podaj liczbę która jest wyższa od poprzedniej:"))
    if number2 < number:
        active = False
    else:
        number = number2
        numbers.append(number2)

print(numbers)
print(f"Średnia z tych liczb wynosi:{sum(numbers) / len(numbers)}")
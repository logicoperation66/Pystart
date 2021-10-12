"""Zadanie 6
Zapytaj użytkownika o długość boku trójkąta równobocznego. Odpowiedz jakie jest pole
tego trójkąta oraz jaka będzie objętość stożka powstała przez obrót tego trójkąta wokół osi,
którą jest jego wysokość ."""

a = int(input('Podaj długość przyprostokątnej "a": '))
b = int(input('Podaj długośc przyprostokątnej "b": '))

pole = (a*b)/2
print(f"Pole trójkąta wynosi {pole}")
objętość_stożka = 1/3*(3.14*b**2*a)
print(objętość_stożka)




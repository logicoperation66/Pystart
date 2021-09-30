'''Odbierz od użytkownika dwa dowolne punkty na płaszczyźnie(x1, y1, x2, y2), które tworzą
odcinek. Znajdź jego środek. i wypisz jakie jest pole oraz promień okręgu, którego ten
odcinek jest średnicą. Poszło? To zastanów się jakie pole i obwód ma prostokąt którego ten
odcinek jest przekątną :-)'''

import math

def center_point():
    """Obliczanie środka odcinka AB"""
    xs1 = (x1+x2)/2
    ys2 = (y1+y2)/2

    return xs1, ys2

def section_lenght():
    """Obliczanie długości odcinka AB"""
    lenght = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return lenght

def circle_field():
    """Obliczanie pola koła o średnicy długości odcinka AB"""
    radius = section_lenght()/2
    field = math.pi*radius**2
    return field

def side_a():
    '''Obliczanie długości boku A'''
    if x1 > x2:
        side_a = x1-x2
    else:
        side_a = x2-x1
    return side_a

def side_b():
    '''Obliczanie długości boku B'''
    if y2 > y1:
        side_b = y2 - y1
    else:
        side_b = y1 - y2
    return side_b

def parimeter():
    '''Wzór na obwód'''
    parimeter = 2*side_b()+2*side_a()
    return parimeter

def rectangle_area():
    side_b()
    side_a()
    area = side_b()*side_a()
    return area



x1 = int(input("Podaj współrzędną x, punktu A :"))
y1 = int(input("Podaj współrzędną y, punktu A :"))
x2 = int(input("Podaj współrzędną x, punktu B :"))
y2 = int(input("Podaj współrzędną y, punktu B :"))


# print(f"Środek odcinka AB ma współrzędne: {center_point()}")
# print(f"Długość odcinka AB wynosi: {round(section_lenght(),2)}")
# print(f"Pole powierzchni koła o średnicy długości odćnika AB wynosi:"
#       f" {round(circle_field(),2)} jednostek kwadratowych")
# print(f"Promień okręgu wynosi {round(section_lenght()/2,2)}")
# print(f"Obwód prostokąta {parimeter()}")

prompt = "Co chcesz znać ?\n1:Współrzędne środka\n2:Długość odcinka " \
         "AB\n3:Pole powierzchni koła o średnicy AB?\n4:Obwód prostokąta " \
         "przekątnej AB\n5:Pole prostokąta o przekątnej AB"

decision = int(input(prompt))

if decision == 1:
    print(center_point())
elif decision == 2:
    print(round(section_lenght(), 2))
elif decision == 3:
    print(round(circle_field(), 2))
elif decision == 4:
    print(parimeter())
elif decision == 5:
    print(rectangle_area())


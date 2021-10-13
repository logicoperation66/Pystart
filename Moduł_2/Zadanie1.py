"""1. Z podanej listy liczb policz te, które są podzielne przez 4 i te które
są podzielne przez 5."""

list = [1, 12, 55, 345, 3255, 123, 8576, 43565, 12354, 144, 66 , 987]
bad_numbers = []
print(f"Lista liczb :{list}")
for item in list:
    if item % 4 == 0:
        print(f"Liczba {item} jest podzielna przez 4")
    elif item % 5 == 0:
        print(f"Liczba {item} jest podzielna przez 5")
    else:
        bad_numbers.append(item)
print(f"Liczby {bad_numbers} są niepodzielne przez cyfrę 4 oraz 5")


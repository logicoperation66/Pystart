'''Przygotuj dwie zmienne, zawierające kurs kupna oraz kurs sprzedaży USD. Na dzień
dzisiejszy to kupno 3.8507, sprzedaż 3,9285. Twoim zadaniem będzie zapytać użytkownika o
to co chce zrobić kupić/sprzedać, następnie zapytać go o ilość złotówek lub dolarów do
wymiany, a następnie poinformować jaką wartość po wymianie użytkownik otrzyma.'''

buy_usd_price = 3.8507
sell_usd_price = 3.9285

choice = int(input("Powiedz co chcesz zrobić kupić(1) sprzedać(2):"))

if choice == 1:
    value = float(input("Podaj ile zł chcesz wymienić:"))
    print(f"Za to dostaniesz {round(value/buy_usd_price, 2)} USD")
else:
    value2 = float(input("Podaj ile dolców chcesz wymienić:"))
    print(f"Za to dostaniesz {round(value2*sell_usd_price, 2)} zł")



'''Pewien program liczy czas tylko w sekundach i resetuje się każdego dnia. Spróbuj zapisać w
klasycznej formie czas przedstawiony w poniższej tabeli:'''

import datetime

time_to_wake = 23400
time_for_lunch = 43200
time_for_sleep = 81000

print(f"{datetime.timedelta(seconds=time_to_wake)} \tPobudka")
print(f"{datetime.timedelta(seconds=time_for_lunch)}\tCzas na lunch")
print(f"{datetime.timedelta(seconds=time_for_sleep)}\tCzas spać")

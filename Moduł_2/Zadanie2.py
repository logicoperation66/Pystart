"""2. Z podanej listy imion o różnej długości znajdź to które jest
najkrótsze i to które jest najdłuższe."""

names = ['Ada', 'Bill', 'Steve', 'Mark', 'Martha']

for name in names:
    if name == min(names):
        print(f'Imie {name} jest najkrótsze na liście.')
    elif name == max(names):
        print(f'Imie {name} jest najdłuższe na liście.')
    else:
        continue

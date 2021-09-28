'''Szef kazał napełniać pracownikowi butelki 330 ml cieczą, w taki sposób by 12% butelki
pozostawało puste. Pracownik umówił się z szefem, że cały płyn który mu pozostanie i nie
wystarczy do napełnienie butelek może zostawić sobie. Po starcie odbierz od użytkownika
informację ile ml płynu dostarczyła fabryka, a wynikiem powinna być ilość cieczy, którą
pracownik będzie mógł wziąć ze sobą :)'''



fluid_value = int(input("Podaj ile ml cieczy otrzymaliśmy :"))
bootle_capacity = 330*0.88
our_stuff = fluid_value % bootle_capacity
print(f"Zostało dla nas {round(our_stuff, 2)}")




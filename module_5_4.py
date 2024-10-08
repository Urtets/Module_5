class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)


ex = Example('data', second=25, third=3.14)
ex2 = Example('Casper', 'dog', third="not a dog")
print(ex, ex2)

from module_5_1 import House

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

print(h1)
print(h2)
print(h3)
# Удаление объектов
del h2
del h3

print(House.houses_history)
print(h1)



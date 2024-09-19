class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        self.number_of_floors += other
        return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors -= other
            return self

    def __rsub__(self, other):
        return other - self.number_of_floors

    def __isub__(self, other):
        if isinstance(other, int):
            self.number_of_floors -= other
            return self

class Human:

    def __init__(self, v_name, surname):
        self.hands = 2
        self.legs = 2
        self.head = 1
        self.name = v_name
        self.surname = surname

    def introduse(self):
        print(f'Меня зовут {self.name}')
        print(f'Фамилия {self.surname}')
        print(f'У меня {self.hands} руки')
        print(f'У меня {self.legs} ноги')
        print(f'У меня {self.head} голова')

    def __repr__(self):
        return self.name


class Child(Human):

    def __init__(self, v_name, surname):
        super().__init__(v_name, surname)
        self.bag = 1

    def introduse(self):
        super().introduse()
        print(f'У меня {self.bag} портфель')


vasya = Human('Вася', 'Якубович')
stas = Child('Стас', 'Костюшкин')


class Bus:

    def __init__(self, v_seats):
        self.row = [0] * v_seats

    def count_seats(self):
        print(f'В автобусе {len(self.row)} мест')

    def watch_bus(self):
        print(self.row)

    def add_child(self, Human):
        for i in range(len(self.row)):
            if self.row[i] == 0:
                self.row[i] = Human
                return self.row

    def delete_child(self, Human):
        for i in range(len(self.row)):
            if self.row[i] == Human:
                self.row[i] = 0
                return self.row

    def child_place(self, Human):
        for i in range(len(self.row)):
            if self.row[i] == Human:
                return (f'Ребенок {Human} сидит на месте {i + 1}')
        else:
            return (f'Ребенка {Human} нет в автобусе')


print(vasya.surname)
bus1 = Bus(12)
bus1.count_seats()
bus1.watch_bus()
print(bus1.child_place(vasya))
bus1.add_child(vasya)
print(bus1.row[0])
bus1.watch_bus()
print(bus1.child_place(vasya))
bus1.add_child(stas)
bus1.watch_bus()
print(bus1.child_place(stas))
bus1.delete_child(vasya)
bus1.watch_bus()
bus1.delete_child(stas)
bus1.watch_bus()

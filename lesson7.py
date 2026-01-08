class Human:
    def __init__(self, name='Ivan'):
        self._name = name
        self._location = "Moscow"   
    
    def set_location(self, location):
        self._location  = location

    def introduce(self):
        return(f'{self._name} : {self._location}')
    
    
class Children(Human):
    def __init__(self, name='Иван'):
        super().__init__(name)  # Вызываем конструктор родительского класса
    
    def set_name(self, name):
        self._name = name

    def set_age(self, age: int):
        self._age = age

class Bus:
    def __init__(self, Human: list):
        self.__children = Human

    def add_children(self, children: list):
        self.__children += children

    def remove_children(self, children: list):
        for n in children:
            if n in self.__children:
                self.__children.remove(n)
    
    def watch_bus(self):
        for n in self.__children:
            print(n.introduce())
    
    def change_location(self, location):
        for n in self.__children:
            n.set_location(location)

misha = Human('Миша')
ivan = Children()
oleg = Children('Олег')
kate = Children('Катя')
bus = Bus([ivan, oleg, kate, misha])
bus.watch_bus()
print('**********************')
bus.change_location('Париж')
bus.watch_bus()
print('**********************')
bus.remove_children([oleg,ivan])
bus.watch_bus()
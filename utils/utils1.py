from datetime import timedelta
from typing import List
import datetime

class Human:
    def __init__(self, name: str, date=datetime.date(1,1,1)):
        self.hands = 2
        self.legs = 2
        self.head = 1
        self.name = name
        self.date = date

    def get_name(self) -> str:
        return f' {self.name} и {self.date}'

    def __str__(self) -> str:
        return self.name


class Rota:
    def __init__(self, humans: List[Human], name: str = "1"):
        self.rota = humans
        self.name = name

    def get_name(self) -> str:
        return self.name

    def add_human(self, human: Human) -> None:
        """Добавление человека в роту"""
        if human not in self.rota:
            self.rota.append(human)
            print(f"Человек {human.get_name()} добавлен в роту {self.name}")

    def remove_human(self, human: Human) -> None:
        """Удаление человека из роты"""
        if human in self.rota:
            self.rota.remove(human)
            print(f"Человек {human.get_name()} удален из роты {self.name}")
        else:
            print(f"Человек {human.get_name()} не найден в роте {self.name}")

    def watch_rota(self) -> None:
        print(f'В роте {self.name} служат солдаты:')
        for human in self.rota:
            print(human.get_name(), end=' ')
        print('\n' + '*' * 30)


class Polk:
    def __init__(self, rotas: List[Rota]):
        self.polk = rotas

    def add_rota(self, rota: Rota) -> None:
        """Добавление роты в полк"""
        if rota not in self.polk:
            self.polk.append(rota)
            print(f"Рота {rota.get_name()} добавлена в полк")

    def remove_rota(self, rota: Rota) -> None:
        """Удаление роты из полка"""
        if rota in self.polk:
            self.polk.remove(rota)
            print(f"Рота {rota.get_name()} удалена из полка")

    def remove_humans_from_polk(self, humans: List[Human]) -> None:
        """Удаление людей из полка (удаляет из соответствующих рот)"""
        for human in humans:
            for rota in self.polk:
                if human in rota.rota:
                    rota.remove_human(human)

    def watch_polk(self) -> None:
        print('В полк входят роты:')
        for rota in self.polk:
            print(rota.get_name(), end=' ')
        print('\n' + '*' * 30)

    def people_in_polk(self) -> None:
        print('В полк входят люди:')
        for rota in self.polk:
            for human in rota.rota:
                print(human.get_name())
        print('\n' + '*' * 30)

from abc import ABC, abstractmethod
import random

class Person(ABC):
    def __init__(self, name, age, money, home):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def make_money(self):
        pass

    @abstractmethod
    def buy_house(self):
        pass

class Human(Person, ABC):
    def __init__(self, name, age, money, home):
        super().__init__(name, age, money, home)

    def info(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old. I have {self.money} money')

    def make_money(self):
        self.money = self.money + 1000
        print(f'{self.name} make 1000 money. Total: {self.money} ')

    def buy_house(self, house):
        if self.money >= house.cost:
            discount = realtor.discount()
            print(f'{self.name}! You can buy this house {house}. Discount for you: {discount}%')
            print(f'Price for you: {(house.cost  - house.cost * discount/100)}!')
            self.money -= house.cost  - house.cost * discount/100
            print(f'{self.name}, you have money: {self.money} ')
        else:
            print(f'{self.name}! Make money!')

class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def house_info(self):
        print(f'House : area = {self.area}, cost = {self.cost}$ ')

    def __str__(self):
        return str(self.area) + ':' + str(self.cost)

class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses):
        self.name = name
        self.houses = houses

    def provide_info(self):
        for i in self.houses:
            i.house_info()

    def steal_money(self, human):
        if random.randint(1, 100) <= 10:
            human.money = 0
            print(f'Help! Realtor {self.name} thief!!!')

    def discount(self):
        return random.randint(0, 20)

h1 = House(40, 7900)
h2 = House(32, 5000)
h3 = House(56, 9200)
realtor = Realtor('Mike', [h1, h2, h3])
realtor.provide_info()
human1 = Human('Bob', 22, 4000, True)
human1.make_money()
human1.make_money()
human1.info()
human2 = Human('Mikle', 21, 5700, False)
human2.make_money()
human2.make_money()
human2.info()
human1.buy_house(h1)
realtor.steal_money(human1)
human2.buy_house(h2)


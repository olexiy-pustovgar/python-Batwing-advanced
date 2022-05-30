# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class

class Animals:
    """
    Parent class, should have eat, sleep
    """
    def __init__(self, species, sex):
        self.species = species
        self.sex = sex
    def move(self):
        print('I am moving')
    def eat(self):
        print('I am hungry')

class Chicken(Animals):
    def __init__(self, species, sex):
        super().__init__(species, sex)
    def say(self):
        print('Ko ko ko')

class Dog(Animals):
    def __init__(self, species, sex):
        super().__init__(species, sex)
    def watch(self):
        print('I guard your house')

class Cat(Animals):
    def __init__(self, species, sex):
        super().__init__(species, sex)
    def caress(self):
        print('I relieve your stress')

class Horse(Animals):
    def __init__(self, species, sex):
        super().__init__(species, sex)
    def walk(self):
        print('I like walking in the rain')

class Duck(Animals):
    def __init__(self, species, sex):
        super().__init__(species, sex)
    def swim(self):
        print('I swim in the river')

if __name__ == '__main__':
    chicken = Chicken('Bird', 'femail')
    print(chicken.species, chicken.sex)
    chicken.say()
    print(isinstance(chicken, Animals))

    dog = Dog('Mammal', 'male')
    print(dog.species, dog.sex)
    dog.watch()
    print(isinstance(dog, Animals))

    cat = Cat('Mammal', 'famail')
    cat.caress()
    cat.eat()
    print(isinstance(cat, Animals))

    horse = Horse('Mammal', 'male')
    horse.move()
    horse.walk()
    print(isinstance(horse, Animals))

    duck = Duck('Bird', 'femail')
    duck.move()
    duck.swim()
    duck.eat()
    print(duck.species, duck.sex)
    print(isinstance(duck, Animals))




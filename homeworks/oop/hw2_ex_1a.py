# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.


from hw2_ex_1 import Animals

class Human:
    """
    Human class, should have eat, sleep, study, work
    """
    def __init__(self, name):
        self.name = name
    def eat(self):
        print('I want to eat!')
    def sleep(self):
        print('I am sleeping')
    def study(self):
        print('Go to school')
    def work(self):
        print('I make program')

class Centaur(Animals, Human):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """
    def __init__(self, name, species, sex):
        Human.__init__(self, name)
        Animals.__init__(self, species, sex)

    def unique_method(self):
        print('I am Centaur!! My name is ', self.name)


centaur = Centaur('Asteriks', 'centaur', 'male')
print(centaur.species)
centaur.unique_method()
centaur.eat()

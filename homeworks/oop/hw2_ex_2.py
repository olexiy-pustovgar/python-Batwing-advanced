# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:

    def __init__(self):
        arm_top = Arm('Arm top')
        arm_down = Arm('Arm down')
        self.arms = [arm_top.slide, arm_down.slide]

class Arm:
    def __init__(self, slide):
        self.slide = slide

person = Person()
print(person.arms)

class CellPhone:
    def __init__(self, screens):
        self.screens = screens

class Screen:
    def __init__(self, resolution):
        self.resolution = resolution

screen_nokia = Screen('16bit 800x600')
screen_samsung = Screen('16bit 800x1440')
screen_lg = Screen('24bit 1080x1920')
screens = [screen_nokia.resolution, screen_samsung.resolution, screen_lg.resolution]

cellphone = CellPhone(screens)
print(cellphone.screens)


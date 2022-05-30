# Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
from abc import abstractmethod, ABC

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass

class HPLaptop(Laptop):
    def __init__(self, hp_screen, hp_keyboard, hp_touchpad, hp_webcams, hp_ports, hp_dynamics):
        self.hp_screen = hp_screen
        self.hp_keyboard = hp_keyboard
        self.hp_touchpad = hp_touchpad
        self.hp_webcams = hp_webcams
        self.hp_ports = hp_ports
        self.hp_dynamics = hp_dynamics

    def screen(self):
        print('Screen ', self.hp_screen)

    def keyboard(self):
        print('Keyboard ', self.hp_keyboard)

    def touchpad(self):
        print('Touchpad ', self.hp_touchpad)

    def webcam(self):
        print('WebCam ', self.hp_webcams)

    def ports(self):
        print('Ports ', self.hp_ports)

    def dynamics(self):
        print('Dynemics ', self.hp_dynamics)

    def __repr__(self):
        return 'You laptop:' + str(list(self.__dict__.values()))

hp_laptop = HPLaptop('Sensor screen', 'membranes keyboard', 'sensitive', 'FullHD', 'Usb3.0 + typeC', 'HiEnd')

print(hp_laptop)

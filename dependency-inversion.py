# https://github.com/ArjanCodes/betterpython

from abc import ABC, abstractmethod

# Interface-Definition. In python ist auch das eine Klasse
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


# dependency - inversion, d.h. hier ist die Klasse nun von einem Interface Switchable (abstract class) 
# abhängig (lose Koppelung) und nicht mehr explizit von einer anderen Klasse wie LightBulb oder
# Fan. Damit kann diese Klasse generischer verwendet werden. 

class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
#
# ein is Ausdruck wird auf TRUE ausgewertet, wenn beide Variablen auf dasselbe (identische) Objekt zeigen
# ein == Ausdruck wird auf TRUE ausgewertet, wenn die Objekte, auf die die Variablen verweisen, gleich sind.

a = [1, 2, 3]
b = a
print("a={}, b={}".format(a, b))
print("a == b")
print(a == b)
print("a is b")
print(a is b)
print("c=list(a)")
c = list(a)
print("a == c")
print(a == c)
print("a is c")
print(a is c)
print("\n\n")


#
# Stringkonvertierung
#
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


my_car = Car('red', 37281)
print(my_car)
print(my_car.color, my_car.mileage)


# anstatt deine eigenen Mechanismen zur Stringkonvertierung aufzubauen, ist es besser, de Methoden __str__ und __repr__
# zu deinen Klassen hinzuzufügen
class Car2:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return 'a {} car.'.format(self.color)


print("\n Class 2 - Beispiel")
my_car2 = Car2('red', 32781)
print(my_car2)
print(str(my_car2))


# in python 3 gibt es zwei Dunder Methoden zur Steuerung der Stringkonvertierung. Neben __str__ gibt es noch __repr__
# __str__ wird bei print () Aufruf verwendet, __repr__ wird verwendet, wenn das Objekt aufgerufen wird oder bei listen
# und dictionaries.
class Car3:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return "__repr__ for Car"

    def __str__(self):
        return "__str__ for Car"


print("\nCar 3 Beispiel")
my_car = Car3('red', 12345)
print(my_car)
print("{}".format(my_car))
print(str([my_car]))
# um manuell zwischen den beiden Stringkonvertierungsmethoden zu wählen, um den Zweck deines Codes klarer auszudrücken,
# solltest du die integrierte Funktion str() und repr() verwenden. Das ist gegenüber dem direkten Aufruf von
# __str__ und __repr__ zu bevorzugen, da es übersichtlicher aussieht
print(str(my_car))
print(repr(my_car))


# __str__ zielt darauf ab, möglichst lesbar zu sein
# __repr__ zielt darauf ab, möglichst genau zu sein

# !! JEDE KLASSE BENÖTGT ZUMINDEST EiNE __repr__ METHODE !!

class Car4:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '{} - {} {}'.format(self.__class__.__name__, self.color, self.mileage)


print("\n\nCar4 Beispiel")
my_car = Car4('red', 54321)
print("repr: ", repr(my_car))
print("str nicht definiert, daher wird repr ausgegeben: ", str(my_car))


# BEST Practice
# Im folgenden siehst du ein vollständiges Beispiel für python3 mit einer optionalen Implementierung von __str__
class Car5:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '{} - {} {}'.format(self.__class__.__name__, self.color, self.mileage)

    def __str__(self):
        return 'a {} car'.format(self.color)


print("\n\nCar5 Best Practice")
my_car = Car5('blue', 12345)
print("repr: ", repr(my_car))
print("str: ", str(my_car))


# ................................................................................................................
# EIGENE AUSNAHMEKLASSEN
# ................................................................................................................
# es kann praktisch sein, seine eigenen Fehlerklassen zu definieren
# um eine Hierarchie für alle eigenen Ausnahmen in einem Modul oder Paket zu erstellen, dekalriere als Erstes eine
# Basisklasse, von der alle konkreten Fehlerklassen erben.
class BasisValidationError(ValueError):
    pass


# von dieser Basisklasse kannst du nun alle echten Fehlerklassen ableiten. dadurch erhälst du mir nur wenig Aufwand
# eine saubere und ordentlche Ausnahmehierarchie
class NameTooShortError(BasisValidationError):
    pass


class NameTooLongError(BasisValidationError):
    pass


class NameTooCuteError(BasisValidationError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


name = "Arne"
try:
    validate(name)
except BasisValidationError as err:
    print(err)

#
# ...................................................................................................................
# Objekte klonen
#
# flache Kopien
print("\nflache Kopien")
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
print(xs)
print(ys)

print("\nflache Kopien erweitern")
xs.append(['new sublist'])
print(xs)
print(ys)

print("\nÄndern eines Elements in xs")
xs[1][0] = 'X'
print("xs=", xs)
print("ys=", ys)
print("Uuupps .... ys wird auch geändert, obwohl nur xs geändert wurde")

print("\ntiefe Kopien")
import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
print("xs=", xs)
print("zs=", zs)
print("\nÄndern eines Elements in xs")
xs[1][0] = 'X'
print("xs=", xs)
print("zs=", zs)
print("zs wird nicht geändert - so wie es sein soll")


#
# ...................................................................
#
# kopieren beliebiger Objekte

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point ({},{})'.format(self.x, self.y)


a = Point(23, 42)
b = copy.copy(a)
print("a=", a)
print("b=", b)
print("a is b = ", a is b)


# Erweiterung einer vielschichtigen Objekthierarchie
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return 'Rectangle tl={}, br={}'.format(self.topleft, self.bottomright)


rect = Rectangle(Point(0, 1), Point(5, 8))
srect = copy.copy(rect)

print("rect=", rect)
print("srect=", srect)
print("rect is srect? ", rect is srect)

print("\nflache Kopie - Ändern eines Punktes in rect")
rect.topleft.x = 999
print("rect=", rect)
print("srect=", srect)
print("rect is srect? ", rect is srect)

print("\ndeep Copy - Ändern eines Punktes in drect")
drect = copy.deepcopy(srect)
drect.topleft.x = 222
print("drect=", drect)
print("srect=", srect)
print("drect is srect? ", drect is srect)

# Abstrakte Basisklassen
# Mithilfe einer abstrakten Basisklasse kannst du dafür sorge tragen, dass abgeleitete Klassen die Methoden
# ais dieser Basisklasse tatsächlich implementieren.
# - eine Instanzierung der Basisklasse sollte unmöglich sein
# - wenn in einer Unterklasse vergessen wurde, Schnittstellenmethoden zu implementieren, sollte so bald wie
#   möglich ein Fehler ausgelöst werden.
# Nutzung von abc (abstract basis class)

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    # wir haben wieder vergessen bar() zu implementieren

assert issubclass(Concrete,Base)

#c = Concrete()
# - Abstrakte Basisklassen sorgen dafür, dass abgeleitete Klassen bestimmte Methoden aus der Basisklasse zur
#   Instanziierungszeit implementieren
# - Abstrakte Basisklassen helfen Bugs zu vermeiden und Klassenhierarchien wartunngsfreundlicher zu gestalten


#
# ......................................................................................................
# Instanz, Klassen und statische Methoden
#
print ('\n\nInstanz, Klassen, statische Methoden')
class MyClass:
    def method(self):
        return 'Instance method called',self
    @classmethod
    def classmethod(cls):
        return 'call method called',cls
    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print ('obj.method():',obj.method())
print ('obj.classmethod():',obj.classmethod())
print ('obj.staticmethod():', obj.staticmethod())

# Beispiel
import math

class Pizza:
    def __init__(self,radius,ingredients):
        self.radius = radius
        self.ingredients = ingredients
    def __repr__(self):
        return ('Pizza {}, {}'.format(self.radius,self.ingredients))
    def area(self):
        return self.circle_area(self.radius)
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, [
    'mozzarella',
    'tomatoes',
    ])

print ('p=',p)
print ('p.area():',p.area())
print ('Pizza.circle_area(4):',Pizza.circle_area(4))
# statische Methoden bieten auch Vorteile beim Schreiben vom Testcode. Da circle_area() vom Rest der Klasse unabhängig
# ist, lässt es sich auch leichter testen. Man kann das wie eine normale Funktion testen (Pizza.circle_area(4))
# - Instanzmethoden benötigen eine Klasseninstanz und können über self darauf zugreifen
# - Klassenmethoden brauchen keine Klasseninstanz. Sie können nicht mit self auf die Instanz zugreifen, aber mit
#   cls auf die Klasse
# - statische Methoden haben werde Zugriff auf cls noch auf self. Sie wirken wie reguläre Funktionen, gehören aber
#   zum Namespace der Klasse
# - Statische und Klassenmethoden machen das vom Entwickler beabsichtigte Design der Klasse deutlich und setzen es bis zu
#   einem gewissen Grad auch durch. Das bietet deutliche Vorteile für die Wartung.


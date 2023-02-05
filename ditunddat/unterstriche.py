'''Dunders
Dunders steht für double underscore

Führender einfacher Unterstrich: _var: Name ist für den internen Gebrauch vorgesehen, wird aber vom python interpreter
                                        nicht durchgesetzt.
Angehängter einfacher Unterstrich: var_: Wird nach Konvention genutzt, um Namenskonflikten mit python schlüsselwörtern
                                        zu vermeiden.
Führender doppelter Unterstrich: __var: Löst im Kontext von Klassen eine Namensumformung aus. Wird vom python interpreter
                                        umgesetzt.
Führender und angehängter Doppelstrich: __var__: Kennzeichnet besondere Methoden, die in python definiert sind. Vermeide
                                        Namen dieser Art für eigene Attribute.
Einzelner Unterstrich: _: wird als temporäre Variable benutzt.'''

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

print ("einfacher Unterstricht vor der Variable")
c = Test()
print ("c.foo {}".format(c.foo))
print ("c._bar {}".format(c._bar))


print ("\n\ndoppelter Unterstrich")
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42
c= Test()

print ("__c.baz wird automatisch umgewandelt in der Form, dass sie nicht überschrieben werden kann")
print (dir(c))

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'override'
        self._bar = 'override'
        self.__baz = 'override'

c2 = ExtendedTest()
print ("\nc2.foo {}".format(c2.foo))
print ("c2._bar {}".format(c2._bar))
try:
  print ("c2.__baz {}".format(c2.__baz))
except AttributeError:
  print ("c2.__baz kann nicht geändert werden, daher würde hier ein Fehler vom Interpreter erzeugt werden.")
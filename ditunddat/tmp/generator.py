# Generator

# f(x) -> __call__

# what is the difference between
#  def add1(x,y):
#       return x + y

# Class Add:
#   def __call__(self, x, y)
#       return x + y
# add2=Add()

# Aus Sicht des Endusers erst einmal kein Unterschied

# Aber ein Zaehler kann man gut mit der Klasse definieren:

from time import sleep

class Add:
    def __init__(self):
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        sleep(1)     # the very long computation
        return self.i

add = Add()

# main (hier wird die Klasse jeweils um +1 erhöht
for ix, x in enumerate(add):
    if ix > 5: break
    print(x)




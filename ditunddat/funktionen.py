# Funktionsbeispiele

# Lambda Funktionen sind kleine, anonyme funktionen.
# in diesem Beispiel kann einer Funktion auch gleich zwei Argumente x y übergeben werden
print ((lambda x,y: x+y)(5,3))

# Beispiel sortieren von einem Tuple nach ihrem zweiten Wert
tuples = [(1,'d'),(2,'b'),(4,'a'),(3,'c')]
print(sorted(tuples, key=lambda x: x[1]))

# Sortierreihenfolge
# -5 -4 -3 -2 -1 0 1 2 3 4 5
#
print ("\n\nsorted(range(-5,6))")
print (sorted(range(-5,6)))

# x*x: 25 16 9 4 1 0 1 4 9 16 25
print ("\nsorted(range(-5,6), key=lambda x: x*x)")
print(sorted(range(-5,6), key=lambda x: x*x))

# folgendes ist keine gute Verwendung von lambdas, da verwirrend
class Car:
    rev = lambda self: print ('Wroom')
    crash = lambda self: print ('Boom!')

myCar = Car()
print ('\n\n', myCar.crash())

# gefährlich
print (list(filter(lambda x: x % 2 == 0, range(16))))
#besser
print ([x for x in range(16) if x % 2 == 0])

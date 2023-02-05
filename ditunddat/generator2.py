from time import sleep

class Foo:
    def __init__(self):
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.i +=1
        sleep(1)
        return self.i

def Foo2():
    i = 0
    while True:
        i += 1
        sleep(1)
        yield i

add=Foo()

print ("Aufruf der Klasse Foo")
for ix, x in enumerate(add):
    if ix > 5: break
    print(x)

print ("Aufruf der Funktion Foo2 mit generator (yield) inside, d.h. die Berechnung wird nicht jedesmal neu gestartet!")
for ix, x in enumerate(Foo2()):
    if ix > 5: break
    print(x)

print ("Macht beides das Selbe, nur die Funktion ist schneller geschrieben ;-)")


print ("Beispiel Fibonaci Zahlen")
print ("lazy implementation:, hier die Iteration frei vorgebbar!!")
def fib(a=1, b=1):
    while(True):
        yield a
        a ,b = b, a + b

for idx, x in enumerate(fib()):
    if idx > 9: break
    print (x)

print ("eager implementation, hier muss man die Iteration vorgeben!!")
def fib(a=1, b=1):
    rv = []
    for _ in range(10):
        rv.append(a)
        a ,b = b, a+b
    return rv

print (fib())


##
print ("Anderes Beispiel - Sequence erzeugen, d.h. erst Methode a, dann b, dann c aufrufen ")
print ("Lösung über Generator")

def first():
    print ("First")
    return

def second():
    print ("Second")
    return

def last():
    print ("last")
    return


def foo_sequence():
    first()
    yield
    second()
    yield
    last()
    yield

f = foo_sequence()
next(f)
next(f)
next(f)


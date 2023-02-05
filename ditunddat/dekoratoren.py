''' Dekoratoren machen es möglich, das Verhalten von aufrufbaren Objekten (Funktionen, Methoden, Klassen) zu
    erweitern und abzuwandeln, OHNE diese Objekte dauerhaft zu ändern'''

''' Eine Dekorator ist ein aufrufbares Objekt, das ein aufrufbares Objekt als Eingabe annimmt und ein anderes
    aufrufbares Objekt zurückgibt.'''

# NULL Dekorator
def null_decorator(func):
    return func

# das objekt null_decorator ist aufrufbar - es ist eine Funktion - es nimmt ein anderes aufrufbares Object als
# Eingabe entgegen und es gibt diese aufrufbare Eingabe unverändert wieder zurück. Damit wollen wir nun eine andere
# Funktion dekorieren.
def greet():
    return ("Hello!")

greet = null_decorator(greet)
print (greet())

# Anstatt null_decorator ausdrücklich für greet aufzurufen und dann die Variable greet neu zuzuweisen, kann man die
# Schreibweise @ nutzen, um eine Funktion auf komfortable Weise zu dekorieren.

@null_decorator
def greet():
    return ("Hello World!")

print (greet())


#
# Dekoratoren können das Verhalten ändern
#
# folgender Dekorator wandelt das Ergebnis der dekorierten Funktion in Großbuchstaben um
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

print (greet())


# Mehrere dekoratoren aufrufen, dekoratoren werden von unten nach oben aufgerufen
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'

print (greet())

# funktionen dekorieren, die Argumente entgegennehmen
def proxy(func):
    def wrapper(*args, **kwargs):       # sammeln aller Argumente
        return func (*args, **kwargs)   # und übergabe an Ursprungsfunktion
    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print ('TRACE: calling {}() with {},{}'.format(func.__name__,args, kwargs))
        original_result = func(*args, **kwargs)
        print('TRACE: calling {}() returned {}'.format(func.__name__, original_result))
        return original_result
    return wrapper

@trace
def say(name, line):
    return (name + ': ' + line)

print (say('Jane', 'Hello, World!'))

# Debuggingfähige Dekoratoren schreiben
# wird ein dekorator verwendet, dann werden gewisse Metadaten von der Dekoratorfunktion überlagert. Das macht das
# debugging schwer. Dafür gibt es eine dekoratorfunktion functools.wraps()
import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """return a friendly greeting."""
    return ("Hello")

print (greet.__name__)
print (greet.__doc__)
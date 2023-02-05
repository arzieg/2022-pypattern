# coding=utf-8
# Metaprogramming
# Ziel: Don't repeat yourself
# Anstatt für jede Funktion eine Zeitmessung zu schreiben, kann dies auch einmal als Wrapper geschrieben werden
# durch @ wird der Wrapper for der Funktion ausgeführt.
# Der Wrapper ist so allgemein geschrieben, dass jede beliebige Funktion inkl. aller Argumente übergeben werden kann.
# Dies erreicht man duch (*args, **kwargs)


# Wrapperfunktion
import time
from functools import wraps

def timer(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)                    # hier wird ebenfalls ein Decorator aufgerufen, der Wraper wraps. Dieser enthält
                                    # Information über die aufrufende Funktion (__module__, __name__, __doc__, __dict__)
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print ("Funktion:", func.__name__, "Zeit:", end-start)
        return result
    return wrapper

@timer
def add(x,y=10):
    return x+y

@timer
def sub(x,y=10):
    return x-y

# main

print ("add(10)",    add(10))
print ("add(20,30",  add(20,30))
print ('add("a","b")', add('a', 'b'))
print ("sub(10)",    sub(10))
print ("sub(20,30)", sub(20,30))

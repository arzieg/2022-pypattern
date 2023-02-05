# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:12:38 2017

@author: arne
"""

class MyClass:
    """A simple example class"""
    i=12345
    def f(self):
        return ("Hello World")


x=MyClass()
print (x.f())  # Ausgabe 
x.counter = 1
while x.counter < 10: 
    x.counter = x.counter *2
print(x.counter)
del x.counter
  
  
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    
x = Complex(3.0, -4.5)
print ("x.r=", x.r)
print ("x.i=", x.i)

# Funktionsdefinition außerhalb der Klasse
def f1 (self,x,y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return("Hello World Class C")
    h=g

y = C()
print (y.g())
print (y.f(3,4))

class Bag:
    def __init__(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)
        
z=Bag()         # initiiere z
z.add(5)        # fuege 5 zur liste
z.addtwice(10)  # füge 2 x 10 zur Liste
print (z.data)  # gebe liste aus


    
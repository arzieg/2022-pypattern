# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:41:32 2017

@author: arne
"""

class Reverse:
    """Iterator für looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return(self)
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]
        
rev = Reverse ("Hallo World")
#iter (rev)
for char in rev: 
    print (char)
    
    
# andere Implementierung
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
    
for char in reverse("golf"):
    print (char)    

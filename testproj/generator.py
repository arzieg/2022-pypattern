# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:11:56 2017

@author: arne
"""

print (sum(i*i for i in range(10)))   #Summe der Quadrate

xvec = [10,20,30]
yvec = [7,5,3]
xskal= sum(x*y for x,y in zip(xvec,yvec))    # Skalarprodukt
print("Skalarprodukt=",xskal)


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print ("sine_table=",sine_table)


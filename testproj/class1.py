# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:04:43 2017

@author: arne
"""

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("Nach der lokalen Zuweisung:", spam)
    do_nonlocal()
    print("Nach der nonlocal Zuweisung:", spam)
    do_global()
    print("Nach der globalen Zuweisung:", spam)
    
scope_test()
print ("Im globalen Gültigkeitsbereich:", spam)
 
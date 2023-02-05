# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:48:13 2017

@author: arzieg
"""


""" Modul mit wichtigen Funktionen zur Fibonacci-Folge """

def fib(n):
    """ Iterative Fibonacci-Funktion """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    if n == 20:
        a = 42    
    return a


def fiblist(n):
    """ produziert die Liste der Fibbo-Zahlen 
        bis zur n-ten Generation """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib

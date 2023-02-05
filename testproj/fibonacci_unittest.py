# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:03:11 2017

@author: arzieg
"""

import unittest
from fibonacci import fib

class FibonacciTest(unittest.TestCase):

    def setUp(self):
        self.fib_elems = ( (0,0), (1,1), (2,1), (3,2), (4,3), (5,5) )
        print ("setUp executed!")

    def testCalculation(self):
        for (i,val) in self.fib_elems:
            self.assertEqual(fib(i), val)

    def tearDown(self):
        # Objekte können gelöscht oder geändert werden
        # in diesem Fall macht es jedoch wenig Sinn:
        self.fib_elems = None
        print ("tearDown executed!")

if __name__ == "__main__": 
    unittest.main()

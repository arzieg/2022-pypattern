import pytest
#from tdd.mycode import *
from src.tdd.mycode import *
#import tdd.mycode

# Testdriven Development
# https://medium.freecodecamp.org/learning-to-test-with-python-997ace2d8abe

# Idee:
#  1. Schreibe einen Test
#  2. run code und erzeuge Fehler
#  3. Schreibe einen Code, damit Fehler nicht mehr auftritt (das eigentliche Hauptprogramm)
#  4. run und pass Test
#  5. refactor code, z.B erweitern um weitere Funktionalitäten, d.h. beginne wieder bei 1

class Test1Class(object):
    def test_hello(self):
        assert hello_world() == 'hello world'

    def test_custom_num_list(self):
        assert len(create_num_list(10)) == 10

    def test_custom_func_x(self):
        assert custom_func_x(3,2,3) == 54

    def test_custom_non_lin_num_list(self):
        assert custom_non_lin_num_list(5,2,3)[2] == 16
        assert custom_non_lin_num_list(5,3,2)[4] == 48

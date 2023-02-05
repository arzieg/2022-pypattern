# hierzu gehört /tests/tdd.py

import sys


def main(argv=sys.argv):
    print(argv)
    return 0

def hello_world():
    return 'hello world'

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x,const,power):
    return const * (x) ** power

def custom_non_lin_num_list(length, const, power):
    return [custom_func_x(x,const, power) for x in range(length)]

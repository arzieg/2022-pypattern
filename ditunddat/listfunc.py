#!/usr/bin/env python3
import ast
import sys

'''
listfunc.py 
 Aufgabe: Anzeige der definierten Funktionen in einen Python - Script
 Aufruf: listfunc.py <Filename.py>
'''

def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(filename)
        tree = parse_ast(filename)
        for func in top_level_functions(tree.body):
            print("  %s" % func.name)

# content of test_module.py

import os.path
import sys


'''Sometimes tests need to invoke functionality which depends on global settings or which invokes code which cannot be 
easily tested such as network access. The monkeypatch fixture helps you to safely set/delete an attribute, 
dictionary item or environment variable or to modify sys.path for importing. '''

def getssh(): #pseudo application core
    return os.path.join(os.path.expanduser("~admin"), '.ssh')

def test_mytest(monkeypatch):
    def mockreturn(path):
        return '/abc'
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    x = getssh()
    assert x == '/abc/.ssh'


# stdout, stderr
def test_myoutput(capsys): # or use capdf for file descriptot level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print ("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"

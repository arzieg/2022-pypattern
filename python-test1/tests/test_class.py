import pytest


# content of test_class.py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')

    # list the name tmpdir in the test function signature and pytest will lookup and call a fixture
    # factory to create the resource before performing the test function call
    # tmpdir ist eine Build - In Funktion in pytest.
    # Anzeigen aller Build In Funktionen durch pytest --fixtures
    def test_three(self, tmpdir):
        print(tmpdir)
        assert 0

    # in diesem Fall soll ein ZeroDivisionError erzeugt werden, also der Test ist das erfolgreich! Hierfür kann
    # die raise - Methode verwendet werden.
    def test_four(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0

    # excinfo is a ExceptinInfo Instance, which is a wrapper arround the actual exception
    # the main attributes of interest are .type, .value, .traceback.
    # Dies kann also angewendet werden, wenn man die aktuelle Fehlermeldung nicht kennt
    def test_recursion_depth(self):
        with pytest.raises(RuntimeError, message="Runtime Error") as excinfo:
            def f():
                f()
            f()
        assert 'maximum recursion' in str(excinfo.value)

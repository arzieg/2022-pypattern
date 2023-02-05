from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self,maxbytes=-1):
        pass
    @abstractmethod
    def write(self,data):
        pass

# Beispiel, um die internen Ausgaben zu überschreiben. __repr__ wäre, wenn man in der Shell den Wert für Pair abfragt
# __str__ ist, wenn der Wert mit print abgefragt wird.
class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r}'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3,4)
print (p)
print(type(p))

# Beispiel überschreiben von Methon einer Klasse - hier date
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d= Date(2012,12,21)

print (format(d))
print (format(d,'mdy'))
print ('The date is {:dmy}'.format(d))
print ('The date is {:mdy}'.format(d))

# Making Objects Support the Context-Management Protocol
from socket import socket, AF_INET, SOCK_STREAM
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


from functools import partial
conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
    print(resp)


# pivate und public methoden
class A:
    def __init__(self):
        self._internal = 0   # internes attribut, da _<variable>
        self.public = 1

    def public_method(self):
        """
        public method
        """
        return 'Public Method of A'
    def _internal_method(self):
        """
        internal method
        :return: 
        """
        return 'Internal Method of A'

myclass = A()
print (myclass.public_method())
print (myclass._internal_method())
print (myclass._internal)
print (myclass.public)

class B:
    def __init__(self):
        self.__private = 0           # wichtig hier doppelter __
    def __private_method(self):
        return 'Private Method of B'
    def public_method(self):
        self.__private_method()
        return 'Public Method of B'

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1
        # Does not override B.__private
        # Does not override B.__private_method()
    def __private_method(self):
        return 'Private Method of C'

myclass2 = C()
print (myclass2._C__private)          # hier ändert python dann die interne repräsentation auf _C__private
print (myclass2._C__private_method()) # hier auch
print (myclass2.public_method())

# Calling a Method on a Parent Class
# use super()
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()     # Call parent spam()

a = A()
print (a.spam())
b = B()
print (b.spam())

# ein anderes super() beispiel. Wichtig, es gibt das attribut __mro__, damit kann man sich die Suchreihenfolge
# bei einem Aufruf von super() anschauen
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()

cs = ColoredShape(color='blue', shapename='square')
cs.draw()

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)
    def draw(self):
        self.movable.draw()
        super().draw()

class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass

MovableColoredShape(color='red', shapename='triangle',
                    x=10, y=20).draw()

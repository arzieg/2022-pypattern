# if Abfrage

attr = True

if attr:
    print('attr is true')

if not attr:
    print('attr is false')

if attr is None:
    print('attr is None!')


# access dictionary element
d = {'hello' : 'world'}
print (d.get('hello', 'default_value'))   # print world
print (d.get('thingy', 'default_value'))  # print default_value
# or
if 'hello' in d:
    print(d['hello'])

# manipulate lists
a = [3,4,5]
a = [i+3 for i in a]
print(a)
# or
b = map(lambda i: i+3,a)
for i,item in enumerate(b):
    print(i,item)

# ..........................
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]

for multiplier in create_multipliers():
    print (multiplier(2))

# ...........................
# nutzung von structshape.py
from structshape import structshape
t=[1,2,3]
print(structshape(t))
t2 =[[1,2],[3,4],[5,6]]
print(structshape(t2))
t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
print(structshape(t3))
s='abc'
lt = list(zip(t,s))
print(structshape(lt))
d = dict(lt)
print(structshape(d))


class Base:
    def __init__(self):
        print('Base.__init__')
class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')
class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')
class C(A,B):
    def __init__(self):
        super().__init__()
        print('C.__init__')

c=C()
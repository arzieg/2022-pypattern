# Contextmanager

from sqlite3 import connect
from contextlib import contextmanager

# Typischerweise eines Kontextmanagers: irgendwo gibt es ein Enter und eine Exit Methode
# x = ctx.__enter__
# try:
#  pass
# finally:
# x.__exit__

class contextmanager:
    def __init__(self,g):

        self.g = g
    def __call__(self, cur):
        self.cur = cur
        return self
    def __enter__(self):
        self.gi = self.g(self.cur)
        next(self.gi)
    def __exit__(self, *_, **__):
        try:
            next(self.gi)
        except StopIteration:
            pass

@contextmanager
def temptable(cur):
    cur.execute('create table temp (x int, y int);')
    yield
    cur.execute('drop table temp')

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        for x,y in zip(range(10), range(10,20)):
            cur.execute('insert into temp (x,y) values (?,?)', (x,y))
        for row in cur.execute('select * from temp'):
            print (row)

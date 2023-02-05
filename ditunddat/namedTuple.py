
from collections import namedtuple

Car = namedtuple('Car',[
        'color',
        'milleage',
        ])

mycar = Car('red',3812.4)
print (mycar.color)
print (mycar.milleage)
print ('*mycar:',*mycar)
print ('mycar:',mycar)

# praktische Hilfen durch integrierte Hilfsmethoden bei benannten Tupeln
print ('mycar._asdict():',mycar._asdict())
# json files
import json
print ('json.dump:',json.dumps(mycar._asdict()))

# replace methode
mycar._replace(color='blue')
print ('mycar._replace:',mycar._replace(color='blue'))

# neue Instanzen erzeugen eines Tuples mit _make
print (Car._make([
    'red',
    999,
    ]))
# collection.namedtuple ist eine speicherfreundliche Abkürzung, um in python manuell eine unveränderliche Klasse zu definierne
# Benannte Tuple können dir helfen, eine leichter verständliche Strukturierung der Daten zu erzwingen
# Benannte Tuple stellen praktische Hilfsmethoden bereit, deren Namen zwar alle mit einem einfachen Unterstrich beginnen,
#  die aber trotzdem zur öffentlichen Schnittstelle gehören.



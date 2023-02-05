# in diesem Beispiel hat man eine Funktion, die jeden Tag andere Rückgabewerte hat (bsp. Aktienindices)
# in diesem Fall ist ein UNIT Test wie in testcase_1 schwer möglich, da der Output nicht statisch ist.
# Vorgehen wie folgt:

import unittest
from unittest.mock import patch
import io
import test_2_module

sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
''')

class Tests(unittest.TestCase):
    @patch('test_2_module.urlopen', return_value=sample_data)
    # In diesem Beispiel wird die urlopen-Funktion von test_2_module durch ein mock-Objekt ausgetauscht, welches
    # ein BytesIO() Ergebnis zurückliefert.
    def test_dowprices(self, mock_urlopen):
        p = test_2_module.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT': 27.72})
if __name__ == '__main__':
    unittest.main()

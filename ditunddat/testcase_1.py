# Testcase #1
# ein Programm schreibt nach sys.stdout. unittest.mock module’s patch() function kann dies abgreifen, darauf
# kann eine Auswertung erfolgen

# die zu testende Funktion

def urlprint (protocol, host, domain):
    url = '{}://{}.{}'.format(protocol,host,domain)
    print (url)

#
# Testprogramm
#
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import test_1_module

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol,host,domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            test_1_module.urlprint(protocol,host,domain)
            self.assertEqual(fake_out.getvalue(), expected_url)


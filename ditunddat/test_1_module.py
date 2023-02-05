# Testcase #1
# test_1_module ein zu testendes Programm. Das Testprogramm ist testcase_1.py

# die zu testende Funktion steht in test_1_module.py

def urlprint (protocol, host, domain):
    url = '{}://{}.{}'.format(protocol,host,domain)
    print (url)


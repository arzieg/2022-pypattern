# Switch / Case Demo
# Switch Case Anweisung gibt es nicht in python, man kann dies aber über funktionen emulieren.

def dispatch_if (operator, x,y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y

print ("Standard if/elif Abfrage:")
print ("2 + 3 = ",dispatch_if('add',2,3))
print ("2 - 3 = ",dispatch_if('sub',2,3))
print ("2 * 3 = ",dispatch_if('mul',2,3))
print ("2 + 3 = ",dispatch_if('div',2,3))
print ("2 blödsinn 3 =", dispatch_if('bloed',2,3))

print ('\nund nun mit einer Funktion')
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()  # get Funktion (operator oder default Wert = None zurückgeben)
print ("2 + 3 = ",dispatch_dict('add',2,3))
print ("2 - 3 = ",dispatch_dict('sub',2,3))
print ("2 * 3 = ",dispatch_dict('mul',2,3))
print ("2 + 3 = ",dispatch_dict('div',2,3))
print ("2 blödsinn 3 =", dispatch_dict('bloed',2,3))



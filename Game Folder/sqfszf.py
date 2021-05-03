from random import *

def test():
    global a
    a = randint(1, 3)
    print('La valeur est :', a)
    return a

test()
if a == 1:
    print('Jai gagné')
elif a == 2:
    print('Je sais pas')
elif a == 3:
    print('Ça va bg ?')

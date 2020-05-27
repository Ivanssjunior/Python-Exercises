import string
from random import *

import random

characters = string.ascii_letters + string.digits + string.punctuation
number = input('Number of passwords? -')
number = int(number)

lenght = input('Password lenght? -')
lenght = int(lenght)

for p in range(number) :
    password = ''
    for c in range(lenght) :
        password += random.choice(characters)
    print(password)
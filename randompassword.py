#Password Generators

#Random generator using Capitals, lowercase, and digits

import random
import string
from random import shuffle

def randompass(n):

    password = []

    [password.append(random.choice(string.hexdigits)) for i in range(n)]
    password.append(random.choice(string.punctuation))
    shuffle(password)

    print ''.join(password)

randompass(8)

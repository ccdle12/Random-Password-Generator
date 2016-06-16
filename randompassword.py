#Password Generators

#Random generator using Capitals, lowercase, and digits

import random
import string
from random import shuffle

def randompass(n):

    user_input = "Enter the desired length of password: "

    password = []

    [password.append(random.choice(string.hexdigits)) for i in range(n)]
    password.append(random.choice(string.punctuation))
    shuffle(password)

    print ''.join(password)

randompass(6)

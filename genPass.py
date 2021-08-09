import string
from random import choice
from random import randint

def generate_password():
    char = string .ascii_letters + string.punctuation + string.digits
    password = "".join(choice(char) for x in range(randint(6,12)))
    return password



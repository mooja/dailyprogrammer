import random
import string

alphabet_table = string.ascii_letters + string.digits + string.punctuation

def generate_password(length=10):
    password = list()
    for i in range(length):
        password.append(random.choice(alphabet_table))
    return ''.join(password)

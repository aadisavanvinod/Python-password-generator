import random
import string
def generate_pwd():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet)for i in range(10))
    return password

password = generate_pwd()
print(f"generated pwd: {password}")
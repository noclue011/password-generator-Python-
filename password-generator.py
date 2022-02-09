import random
import string
# Greets the user
print('hello, Welcome to Password generator!')
# Asks for the length of the password
length = int(input('\nEnter the length of password: '))

all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all,length))

print(password)
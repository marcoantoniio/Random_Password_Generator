from time import sleep
from getpass import getuser
import string
from secrets import choice
username = getuser()
lengh = choice(range(8, 17))
values = string.ascii_letters + string.digits
password = ''.join(choice(values)for t in range(lengh))
with open('passoword.txt', 'w') as f:
    f.write(password)


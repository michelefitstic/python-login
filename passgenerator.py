import random
import string

password = ""
for i in range(random.randint(10, 20)):
    password += random.choice(string.ascii_letters + string.digits + string.punctuation)

print(password)

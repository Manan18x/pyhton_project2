import random
import string


# define the length of the password
pass_len = 8


charValues = string.ascii_letters + string.digits + string.punctuation



password = ""

for i in range(pass_len):
      password += random. choice(charValues)

print("your random password is:", password)
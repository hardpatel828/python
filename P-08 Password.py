# Write a password generator in Python. Be creative with how you generate passwords -strong passwords
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be
# random, generating a new password every time the user asks for a new password.

import random
import string


length = int ( input ( " Enter password length = " ) )
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
password = ""

for i in range ( length ) :
    password = password + random.choice ( characters ) 

print ( " Generated Password = ", password )
import random
import string

def generate_password(length, num_passwords):
    passwords = []
    for i in range(num_passwords):
        password = ''
        for j in range(length):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        passwords.append(password)
    
    return passwords

print("How many characters should the password be?")
length = int(input())

print("How many passwords should be generated?")  
num_passwords = int(input())

passwords = generate_password(length, num_passwords)
for password in passwords:
    print(password)
import random
import string

#Function declaration to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#user input for password length
password_length = int(input("Enter the length of the password: "))

# Generate & display  password
password = generate_password(password_length)
print("Generated Password: ", password)


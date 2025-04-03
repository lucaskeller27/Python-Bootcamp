
# Day 5 Project - Password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("# Welcome to the Password Generator! #")
num_letters = int(input("How many letters would you like?\n-> "))
num_symbols = int(input("How many symbols would you like?\n-> "))
num_numbers = int(input("How many numbers would you like?\n-> "))

password = ""

for x in range(1, (num_letters + 1)):
    password += random.choice(letters)
    
for x in range(1, (num_symbols + 1)):
    password += random.choice(symbols)

for x in range(1, (num_numbers + 1)):
    password += random.choice(numbers)

# password_list = list(password)
# random.shuffle(password_list)
# random.shuffle(password_list)
# random.shuffle(password_list)
# password = ''.join(password_list) # Converts the list back into a string

print(f"Your custom-made password is:\n-> {password}")

# google "how to convert a list in to a string python"
# read https://www.w3schools.com/python/module_random.asp
# and https://www.w3schools.com/python/python_for_loops.asp

# try to do by myself the part that Bruno helped me with (commented out above)
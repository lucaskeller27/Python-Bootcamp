
# Day 5 Project - Password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters = [letters, numbers, symbols]

print("# Welcome to the Password Generator! #")
num_letters = int(input("How many letters would you like?\n-> "))
num_symbols = int(input("How many symbols would you like?\n-> "))
num_numbers = int(input("How many numbers would you like?\n-> "))

num_characters = (num_letters + num_symbols + num_numbers)

password = ""

for x in range(1, 4):
    print("")

random.choice(characters[(random.randint(0, 3))])
random.shuffle(characters)

for x in range(1, (num_letters + 1)):
    password += random.choice(letters)
    
for x in range(1, (num_symbols + 1)):
    password += random.choice(symbols)

for x in range(1, (num_numbers + 1)):
    password += random.choice(numbers)
    

print(f"Your custom-made password is:\n-> {password}")

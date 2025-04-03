
# Day 5 Project - Password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Getting user input

print("# Welcome to the Password Generator! #")
num_letters = int(input("How many letters would you like?\n-> "))
num_symbols = int(input("How many symbols would you like?\n-> "))
num_numbers = int(input("How many numbers would you like?\n-> "))

# Getting the requested amount of each type of character

letters_list = random.choices(letters, k=(num_letters))
symbols_list = random.choices(symbols, k=(num_symbols))
nums_list = random.choices(numbers, k=(num_numbers))

# Adding all the characters onto a list

password_list = []
password_list.extend(letters_list)
password_list.extend(symbols_list)
password_list.extend(nums_list)

# Shuffling the list and converting it into a string

random.shuffle(password_list)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your custom-made password is:\n-> {password}")

# Other (longer) method using for loops 

# for x in range(1, (num_letters + 1)):
#     password += random.choice(letters)

# for x in range(1, (num_symbols + 1)):
#     password += random.choice(symbols)

# for x in range(1, (num_numbers + 1)):
#     password += random.choice(numbers)
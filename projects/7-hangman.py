# Day 7 Project - Hangman

import random, os

os.system('cls' if os.name == 'nt' else 'clear')

word_list = ["aardvark", "baboon", "camel"]

# Selecting a word

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"

print(placeholder, "\n")

# Asking the user for a letter

letters_left = word_length
guessed_letters = []

while not letters_left == 0:
    guess = input("Guess a letter:\n-> ").lower()
    # Checking if the guess is correct or not
    answer = ""
    for letter in chosen_word:
        if guess == letter:
            answer += letter
            letters_left -= 1
            guessed_letters.append(letter)
        else:
            answer += "_"
    print(answer)

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

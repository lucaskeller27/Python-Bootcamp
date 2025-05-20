# Day 7 Project - Hangman

import random, os

os.system('cls' if os.name == 'nt' else 'clear')

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives_left = 6
word_list = ["aardvark", "baboon", "camel"]

# Selecting a word

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"

print(placeholder, "\n")

game_over = False
guessed_letters = []


while not game_over:
    # Asking the user for a letter
    guess = input("Guess a letter:\n-> ").lower()
    
    # Checking if the guess is correct or not
    answer = ""
    for letter in chosen_word:
        if guess == letter:
            answer += letter
            guessed_letters.append(letter)
        elif letter in guessed_letters:
            answer += letter
        else:
            answer += "_"
    
    if guess not in chosen_word:
        lives_left -= 1

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n", answer, "\n")
    print(stages[lives_left])
    
    # Checking if the game should end
    
    if lives_left == 0:
        game_over = True
        print(f"You lose. The answer was \"{chosen_word}\". To the gallows!")
    
    if "_" not in answer:
        game_over = True
        print("Congratulations, you win!")

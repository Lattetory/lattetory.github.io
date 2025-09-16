# 250914 5일차

# Day 7 Project
# Making the Hangman Game program

# Step 1


# import random 

# word_list = ["aardvark", "baboon", "carmel"]

# # Todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# chosen_word = random.choice(word_list) 
# print(chosen_word)

# # Todo-2 -Ask the user to guess a letter and assign thier answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letters : ").lower()

# # Todo-3 -Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is. "Wrong" if it's not.

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# Step 2 


# import random 

# word_list = ["aardvark", "baboon", "carmel"]

# chosen_word = random.choice(word_list) 
# print(chosen_word)

# # Todo-1 - Create a "placeholder" with the same number of blanks as the chosen_word
# # Hint 
# # Create an empty string called placeholder.
# # for each letter in the chosen_word, add _ to placeholer.
# # So if the chosen_word was "apple" placeholder should be _____ with 5 "_" representing each letter to guess.
# # Print out hint.

# placeholder = ""

# word_length = len(chosen_word)

# for position in range(word_length): # word_length 만큼 반복
#     placeholder += "_" # _ 추가

# print(placeholder) 

# guess = input("Guess a letters : ").lower()

# # Todo-2 - Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# # Hint
# # Create an empty string called "display".
# # Loop through each letter in the chosen_word.
# # If the letter at that position matches guess then reveal that letter in the display at that position.
# # e.g. If the user guessed "p" and the chosen_word was "apple", then display should be _ p p _ _ .
# # Print display and you should see the guessed letter in the correct position.
# # But every letter that is not a match is represented with a "_".

# display = ""

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)


# Step 3

# import random 

# word_list = ["aardvark", "baboon", "carmel"]

# chosen_word = random.choice(word_list) 
# print(chosen_word)

# placeholder = ""

# word_length = len(chosen_word)

# for position in range(word_length): # word_length 만큼 반복
#     placeholder += "_" # _ 추가
# # placeholder = word_length * "_" 같은듯..?

# print(placeholder) 

# # Todo-1 - Use a while loop to let the user guess again.
# # Hint
# # Use a while loop to let the user guess again.
# # The loop should only stop once the user has guessed all the letters in the chosen_word.
# # At that point display has no more blanks ("_"). Then you can tell the user they've won. 

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letters : ").lower()

#     display = ""

# # Todo-2 - Change the for loop so that you keep the previous correct.
# # Hint
# # Uptate the for loop so that previous guesses are added to the display string.
# # At the moment, when the user makes a new guess, the previous guess gets replaced by a "_".
# # We need to fix that by updating the for loop.

#     for letter in chosen_word: 
#         if letter == guess:             # 입력한 글자랑 정답글자랑 같으면
#             display += letter           # 입력한 글자를 추가해라 ex_ a
#             correct_letters.append(guess) # 리스트안에 추가해라  
#         elif letter in correct_letters: # 리스트 안에 들어있는 글자가 있으면 ex_ p 
#             display += letter           # 리스트 안의 글자들을 추가해라
#         else:
#             display += "_"
    
#     print(correct_letters)
#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win!")

# # Step 4

# import random 
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\\  |
#  / \\  |
#       |
# ========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\\  |
#  /    |
#       |
# ========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\\  |
#       |
#       |
# ========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# ========
# ''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# ========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# ========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# ========
# ''']

# word_list = ["aardvark", "baboon", "carmel"]

# # Todo-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #  Set 'lives' to equal 6.

# lives = 6

# chosen_word = random.choice(word_list) 
# print(chosen_word)

# placeholder = ""

# word_length = len(chosen_word)

# for position in range(word_length):
#     placeholder += "_" 

# print(placeholder) 

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letters : ").lower()

#     display = ""

#     for letter in chosen_word: 
#         if letter == guess:             
#             display += letter           
#             correct_letters.append(guess) 
#         elif letter in correct_letters: 
#             display += letter           
#         else:                # 단어가 그 위치에 없을 경우
#             display += "_"
#     print(display)

# # Todo-2: - If guess is not a letter in the chosen_word, Then reduce lives by 1.
# #  If lives goes down to 0 then the game should end, and it should print "You lose."

#     if guess not in chosen_word: # 단어 자체가 없을 경우
#         lives -= 1
#         if lives <= 0:
#             game_over = True
#             print("You lose.")

#     if "_" not in display:
#         game_over = True
#         print("You win!")

#     print(stages[lives])
# # Todo-3: - Print the ASCII art from 'stages'
# #  That corresponds to the current number of lives the user has remaining.


# Step 5

import random 

from Day7_hangman_word import word_list

# from hangman_art import stages, logo > 없어서 패스

# Todo-1: - Update the word list to use the 'word_list' from hangman_words.py

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========
''', '''
  +---+
  |   |
      |
      |
      |
      |
========
''']
logo = ['''
 -
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | | 
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |
                   |___/
''']

# word_list = ["aardvark", "baboon", "carmel"]

lives = 6

# Todo-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(logo[0])

chosen_word = random.choice(word_list) 
# print(chosen_word)

placeholder = ""

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_" 

print(f"Word to Guess : {placeholder}") 

game_over = False
correct_letters = []
overlap_letters = []
while not game_over:

# Todo-6: - Update the code below to tell the user how many lives they have left.
    print(f"******************{lives}/6 LIVES LEFT******************")
    guess = input("Guess a letters : ").lower()

# Todo-4: - If the user has entered a letter they've already guessed, print the lef them know.
# We should not deduct a life for this.
# e.g You've already guessed a, 
    if guess in correct_letters or guess in overlap_letters:
        print(f"You've already guessed : {guess}")

    display = ""

    for letter in chosen_word: 
        if letter == guess:             
            display += letter           
            correct_letters.append(guess) 
            overlap_letters.append(guess)
        elif letter in correct_letters: 
            display += letter           
        else:                
            display += "_"
    print(f"Word to guess : {display}\n")
    
    # Todo-5: - If the letter is not in the chosen_word, print out the letter and let them know.
# e.g You guessed b, that's not in the word, You lose a life.

    if guess not in chosen_word and guess not in overlap_letters: 
        overlap_letters.append(guess)
        print(f"You guessed {guess}, that's not in the word, You lose a life.")
        lives -= 1
        if lives <= 0:
            game_over = True

            # Todo-7: - Update the print statement below to give the user the correct word
            print("******************You lose******************")
            print(f"It was <{chosen_word}>")

    if "_" not in display:
        game_over = True
        print("******************You win!******************")

# Todo-2: - Update the code below to use the stages List from the file hangman_art.py
    
    print(stages[lives])

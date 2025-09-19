# 250918~19 Day 9 ~ 10 of Python

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(enemies) # 2 

# increase_enemies()
# print(enemies) # 1


# Local Scope 지역 범위

# def drink_potion():
#     potion_strengh = 2
#     print(potion_strengh)

# drink_potion()
# print(potion_strengh) # 오류 나는 이유 = 함수 안에서만 실행 되는 변수라서
# # drink_pition 안에서만 potion_strengh 실행 가능

# Global Scope 전역 범위

# player_health = 10

# def drink_potion():
#     potion_strengh = 2
#     print(player_health) # 위에서 전역변수 선언 했기때문에

# drink_potion() # 안에서도 실행 가능

# There is no Block Scope in python 파이썬엔 블록 유효범위 없음 

# 전역범위와 전역범위 내에서 무언가 수정하는 개념
# Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     global enemies # 전역변수 쓸수있게함 하지만 오류가 있음
#                    # 그래서 최대한 지역안에선 전역변수를 수정하지말길! 
#     enemies = 2
#     print(enemies) # 2 

#    아래 처럼 return 활용하기!

# enemies = 1

# def increase_enemies(enemy):
#     print(enemies)
#     return enemy + 1

# enemies = increase_enemies(enemies)
# print(enemies)

# Global Constants  절대 안바꿀 변수는 모두 대문자로 약속


# 소수 확인기

# def is_prime(num):
#     b = []

#     for a in range(1, num+1):
#         if (num % a) == 0:
#             b.append(a)
#     if len(b) > 2 :
#         return False
#     else: 
#         return True
# is_prime(73)


# Day 12 Project
# Making the Number Guessing Game project

# 내가 찾은 답!

# import random

# randnum = random.randint(1, 100)

# print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# game_over = False

# life = 0

# if level == "easy":
#     life = 10
# elif level == "hard":
#     life = 5
# else:
#     print("Refresh the page to run again.")
#     game_over = True

# def lifes():
#     print(f"You have {life} attempts remaining to guess the number.")

# def decrease_enemies(lifess):
#     return lifess - 1

# while not game_over:
#     lifes()
#     life = decrease_enemies(life)
#     guessnum = int(input("Make a guess:"))
    
#     if guessnum == randnum:
#         print(f"You got it! The answer was {randnum}.")
#         print("Refresh the page to run again.")
#         game_over = True
#     elif life == 0:
#         print("You've run out of guesses. Refresh the page to run again.")
#         game_over = True
#     else:
#         if guessnum > randnum:
#             print("Too high")
#         elif guessnum < randnum:
#             print("Too low")

# 정답

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(user_guess, actual_answer, turns): # 여기에 turns 넣어서 전역변수 사용
    '''Checks answer against guess, returns the number of turns remaining.'''
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        global turns
        return EASY_LEVEL_TURNS
    elif level == "hard":
        global turns
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return 
        elif guess != answer:
            print("Guess again.")
game()


# 250911 2일차

# student_scores = [150, 190, 200, 135, 100, 110, 170]

# # sum 1
# sums = 0
# for score in student_scores:
#     sums += score
# print(sums)

# # sum 2
# total_student_scores = sum(student_scores)
# print(total_student_scores)

# # max 2
# max_student_scores = max(student_scores)
# print(max_student_scores)

# # max 1
# max = 0
# for score in student_scores:
#     if score > max:
#         max = score
# print(max)


# # range(a, b, c) a ~ b-1 c간격만큼
# total = 0
# for number in range(1, 101): # 1 ~ 9
#     total += number
# print(total)


# FizzBuzz Game
# for num in range(1,101):
#     if (num % 3) == 0 and (num % 5) == 0:
#         print("FizzBuzz")
#     elif (num % 3) == 0:
#         print("Fizz")
#     elif (num % 5) == 0:
#         print("Buzz")
#     else:
#         print(num)


# Day 5 Project
# Making the Password Generator program
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy level ver.
# password = ""
# for str in letters: # for str in range(0, nr_letters) 를 적는다면
#     if nr_letters <= 0: # 여기 생략 가능 
#         pass
#     else:
#         password += random.choice(letters) # 바로 이것만 적으면 됨
#         nr_letters -= 1  # 여기 생략 가능

# for sym in range(0, nr_symbols): # 이렇게
#         password += random.choice(symbols)

# for num in range(0, nr_numbers):
#         password += random.choice(numbers)

# print(password)


# Hard level ver.
password = []
for str in range(0, nr_letters): 
    str = random.choice(letters) # password.append(random.choice(letters))
    password.append(str)         # 로 바꾸면 줄일수있음
for sym in range(0, nr_symbols):
    password.append(random.choice(symbols)) # 이렇게
for num in range(0, nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password) # 리스트를 순서 랜덤으로 바꿈

print(f"Your password is : {''.join(password)}") # 리스트를 문자열로 바꿈

# 혹은
# passwords = ""
# for char in password
#   passwords += char
# print(f"Your password is : {passwords}") # 이렇게도 가능인데 ''.join()이 좋은듯



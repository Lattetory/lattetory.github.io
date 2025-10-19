# 250914 ~ 250916 5~7일차

# def my_function(something):  > somethig = parameter (매개변수)-> 전달되는 데이터의 이름
#     print("hello")                                   
#     print("how are you")
#     print("?")

# my_function(123)            > 123 = argument (인자)-> 데이터의 실제값
# my_function()
# my_function()

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print("Isn't the weather nice?")

# greet_with_name("latte")


# def life_in_weeks(age):
#     current_age = (age) * 52
#     life_week = 90 * 52
#     left_week = life_week - current_age
#     print(f"You have {left_week} weeks left.")


# Functions with more than 1 input

# # life_in_weeks(56)
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"I'm from {location}")

# greet_with("Latte", "Korea")
# greet_with(location="Korea", name="Latte") # 키워드 인자


# def calculate_love_score(name1, name2):
#     name = name1.lower() + name2.lower()

#     true = ["t","r","u","e"]
#     love = ["l","o","v","e"]

#     count = 0

#     for letter in name:
#         if letter in true:
#             count += 7
#         if letter in love:
#             count += 9

#     print(count)

# calculate_love_score("Moon Latte", "Moon Jintol")


# Day 8 Project
# Making the Caesar Cipher program

# Step 1

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# Todo-1 : Create a function called 'encrypt()' that takes 'original_text' and 'shift_text' as 2 inputs.
# Todo-2 : Inside the 'encrypt()' function, shift each letter of the 'original_text' forwords in the alphabet 
#          by the shift amount and print the encrypt text.
# Hint
# You can use the built-in Python index() function to find out the position of an item in a list.

# 내가 찾은 답!
# original_text = []
# shift_amount = []
# def encrypt(original_text, shift_amount):
#     for letter in text:
#         if letter in alphabet:
#             original_text = alphabet.index(letter)
#             if original_text >= 25: # 이건 리스트의 길이를 알때만 사용가능한거였군
#                 original_text = original_text - 26
#             shift_amount += alphabet[original_text + shift]

#     print(f"Here is the encoded result: {"".join(shift_amount)}") 

# encrypt(original_text, shift_amount)


# 정답
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) # 리스트의 길이를 몰라도 사용가능 ex_34 % 25 = 9
#         cipher_text += alphabet[shifted_position] 
#     print(f"Here is the encoded result: {cipher_text}") 

# encrypt(original_text=text, shift_amount=shift)


# Todo-4 : What happens if you try to shift z forwards by 9? Can you fix the code?

# Todo-3 : call the 'encrypt()' function and pass in the user inputs. 
#          You should be able to test the code and encrypt a message.

# Step 2

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) # 리스트의 길이를 몰라도 사용가능 ex_34 % 25 = 9
#         cipher_text += alphabet[shifted_position] 
#     print(f"Here is the encoded result: {cipher_text}") 

# # Todo-1 : Create a function called 'decrypt()' that takes 'original_text' and 'shift_text' as 2 inputs.
# # Todo-2 : Inside the 'decrypt()' function, shift each letter of the 'original_text' forwords in the alphabet 
# #          by the shift amount and print the encrypt text.

# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet) 
#         cipher_text += alphabet[shifted_position] 
#     print(f"Here is the encoded result: {cipher_text}") 

# Todo-3 : Combine the 'encrypt()' and 'decrypt' function into one function called caesar().
#          Use the value of the user chosen direction variable to determin which functionallity to use.
#          Call the caesar function instead of encrypt/decrypt and pass in all three variable. 
#          direction / text / shift.

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1 # 양수를 음수로 바꾸는 법
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) 
#         output_text += alphabet[shifted_position] 
#     print(f"Here is the {encode_or_decode}d result: {output_text}") 
#                         > encoded / decoded
# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# 최종 
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1 
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) 
#         output_text += alphabet[shifted_position] 
#     print(f"Here is the {encode_or_decode}d result: {output_text}") 

# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


# Step 3

# Todo-1 : Import and print the logo from art.py when the program starts.
# 난 없으므로 직접 한다 ㅋ
# import art
# print(art.logo)

# logo = ['''
        
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'    "8
# 8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
# "8a    ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88
#                           88
#                           88
#            ""             88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP""""""" 88
# "8a    ,aa 88 88P,   ,a8" 88       88 "8b,   ,aa 88
#  '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88
#               88
#               88
# ''']
# print(logo[0])

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # Todo-2 : What happens if the user enters a number/symbol/space?
# # ex) meet me at 3! > xxxx xx xx 3!

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     if encode_or_decode == "decode":
#         shift_amount *= -1 
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet) 
#             output_text += alphabet[shifted_position] 
#     print(f"Here is the {encode_or_decode}d result: {output_text}\n") 

# # 내가 찾은 답! 헤헤 내가 더 짧당
# # def start():
# #     direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
# #     text = input("Type your message:\n").lower()
# #     shift = int(input("Type the shift number:\n"))
# #     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
# #     print("Can you figure out a way ro restart the cipher program?")
# #     answer = input("Type 'yes' if you want to go again. Otherwise, type 'no\n").lower()
# #     if answer == "yes":
# #         start()
# #     else:
# #         print("\nGood bye!")

# # # Todo-3 : Can you figure out a way ro restart the cipher program?
# # #          Type 'yes' if you want to go again. Otherwise, type 'no'
# # #          If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.

# # start()

# # 정답
# should_continue = True

# while should_continue:
#     direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("\nGood bye")


# 최종

logo = ['''
        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'    "8
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
"8a    ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88
                          88
                          88
           ""             88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a    ,aa 88 88P,   ,a8" 88       88 "8b,   ,aa 88
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88
              88
              88
''']
print(logo[0])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1 
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet) 
            output_text += alphabet[shifted_position] 
    print(f"Here is the {encode_or_decode}d result: {output_text}\n") 

def start():
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    print("Can you figure out a way ro restart the cipher program?")
    answer = input("Type 'yes' if you want to go again. Otherwise, type 'no\n").lower()
    if answer == "yes":
        start()
    else:
        print("\nGood bye!")

start()
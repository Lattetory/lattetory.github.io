# 250910 1일차

# # Subscripting
# print("Latte"[1])
# print("Latte"[-4])

# # String
# print("123" + "456")

# # Integer = Whole number
# print(123 + 456)

# # Large Integers ( 단위 구분 "," 역할 _ 개발자가 단위 구분하기 편함)
# print(123_456_789)

# # Float = Floating Point Number
# print(3.14159)

# # Boolean
# print(True)
# print(False)

# type check
# print(type("Hello"))
# print(type(123))
# print(type(3.14))
# print(type(True))
# print("123" + "456")
# print(int("123") + int("456"))


# # 1
# print("Number of letters in your name: " + str(len(input("Enter your name"))))
# # 2
# name = input("Enter your name")
# length = len(name)
# print(f"Number of letters in your name: {length}")
# # 3
# print(f"Number of letters in your name: {len(input("Enter your name"))}")


# round (반올림변수, 자릿수)
# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(int(bmi)) # 그냥 소숫점 삭제
# print(round(bmi, 2)) # 반올림, 둘째 자리수까지


# Day 2 Project
# Making the Tip calculator program

print(f"Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = (int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100) + 1
people = int(input("How many people to split the bill? "))
pay = round((bill * tip) / people, 2)
print(f"Each person should pay : ${pay}")

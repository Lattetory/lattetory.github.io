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









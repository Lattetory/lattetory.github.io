# 250911 2일차

import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10 # 0.0 <= n < 1.0
# print(random_number_0_to_1)

# 위 아래 비슷한 값을 얻을 수 있지만 아래는 반올림에 따라 1.0이 나올수있음
# 범위를 확실하게 하고 싶으면 위 random.random() 으로 _ 1 절대 안나오니까
# 가능한 위 코드를 하는게 좋음

# random_float = random.uniform(1, 10) # 0.0 <= n <= 1.0
# print(random_float)

# coin Heads or Tails
# coin = random.randint(0, 1)
# if coin == 0:
#     print("Heads")
# else:
#     print("Tails")

# # Banker Roulette 1
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# roulette = random.randint(0, 4)
# print(friends[roulette])

# # Banker Roulette 2
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friends))


# Day 4 Project
# Making the Rock Paper Scissors Game program

rock = '''
    _ _ _ _
---'  _ _ _)
    ( _ _ _ )
    ( _ _ _ )
    ( _ _ _ )
---._( _ _ )
'''

paper = '''
    _ _ _
---'  _ _ )_ _ _ 
        _ _ _ _ )
        _ _ _ _ )
        _ _ _ _ )
---. _ _ _ _ )
'''

scissors = '''
        _ 
    ---'_ )_ _ _
        ( _ _ _ )
        ( _ _ _ )
        (_ _)
---. _ _(_ )
'''

# 정답 / 맨아래 코드가 최종 코드
# list = [rock, paper, scissors]
# user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
# print(list[user]) # 근데 이거 아닌거 같은데.. 리스트 벗어나면 내 답이 맞는듯?
# computer = random.randint(0, 2)

# print("Computher Chose:")
# print(list[computer])

# if user >= 3 or user < 0:
#     print("You typed an invalid number. You lose")
# elif user == 0 and computer ==2:
#     print("You win!")
# elif computer == 0 and user ==2:
#     print("You lose!")
# elif computer > user:
#     print("You lose")
# elif user == computer:
#     print("Draw!")

# 내가 한 답은 너무 길다

# list = [rock, paper, scissors]
# computer = random.choice(list)
# user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
# computer = random.randint(0, 2)
# if user >= 3 or user <= -1:
#     print("You typed an invalid number. You lose!")
# else:
#     print(list[user])
#     print(f"Computer choose: {computer}")

#     if user == 0:
#         if computer == list[0]:
#             print("Draw")
#         elif computer == list[1]:
#             print("You lose")
#         else:
#             print("You win")

#     elif user == 1:
#         if computer == list[0]:
#             print("You win")
#         elif computer == list[1]:
#             print("Draw")
#         else:
#             print("You lose")

#     elif user == 2:
#         if computer == list[0]:
#             print("You lose")
#         elif computer == list[1]:
#             print("You win")
#         else:
#             print("Draw")


### 최종 합치기 _ 이거쥐~
list = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer = random.randint(0, 2)
if user >= 3 or user <= -1:
    print("You typed an invalid number. You lose!")
else:
    print(list[user])
    print("Computer choose:")
    print(list[computer])
    if user == 0 and computer ==2:
        print("You win!")
    elif computer == 0 and user ==2:
        print("You lose!")
    elif user > computer:
        print("You win!")
    elif computer > user:
        print("You lose")
    elif user == computer:
        print("Draw!")
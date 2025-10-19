# 250920~23 Day 11~14 of Python

# Day 14 Project
# Making the Higher-Lower Game project


# 내가 찾은 답!!! 야호 + 정답보고 최종 수정함! 
# 아 근데 저기 예시랑 다르긴해서 유데미 정답이랑은 다르겠다..

import random
from Day14_game_data import data

# 순서
# 간단하게 생각해보자
# 랜덤 생성 함수
def randpick():
    rand_team = random.choice(data)
    data.remove(rand_team)
    return rand_team

# 랜덤 생성 저장, 저장 2
P2 = randpick() 
P1 = P2         
score = 0
play = True 

while play == True:
    if len(data) == 0:
        print(f"Congratulation! Your final score {score}!\n")
        play = False
    else:
        P2 = randpick()
        print(f"Compare A : {P1['club']}, Home: {P1['home']}, Previous_winning_year: {P1['previous_winning_year']}.\n")
        print(f"Against B : {P2['club']}, Home: {P2['home']}, Previous_winning_year: {P2['previous_winning_year']}.\n")

        # 정답 변수
        if P1['wins'] < P2['wins']:
            real_answer = P2
        elif P1['wins'] == P2['wins']:
            print(f"The number of wins is the same. So set the answer to 'A'.\n")
            real_answer = P1
        else:
            real_answer = P1

        # 답변받기
        answer = input("Which team won more? Type 'A' or 'B': ").upper() # 대문자로 
        answers = False

        # 답변 변수
        while answers == False:
            if answer == "A":
                guess_answer = P1
                answers = True
            elif answer == "B":
                guess_answer = P2
                answers = True
            else:
                answer = input("Sorry, that's wrong type. Which team won more? Type 'A' or 'B': ").upper()

        # 랜덤 1, 2 비교
        if guess_answer == real_answer:
            score += 1
            print(f"\nYou're right! Current score: {score}.\n")
            # 맞으면 큰 쪽 저장
            P1 = guess_answer
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            play = False


# 정답!
# 실행만 잘된다면 성공이라함! 아싸 성공! 
# 일단 내 데이터랑 다르지만 정답 적어본다.
# 목표들을 세분화해서 순서 잘 적는게 핵심! 
# 쉬운 것부터 해결해나가기.

# # Display art
# from art import logo, vs
# from game_data import data
# import random


# def format_data(account):
#     """Takes the account data and returns the printable format."""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}."

# def check_answer(user_guess, a_followers, b_followers):
#     """Take a user's guess and the follower counts and returns if they got it right."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"

# print(logo)
# score = 0
# game_should_continue = True
# account_b = random.choice(data) # 아하 이렇게하면 글로벌 안써되되네

# # Make the game repeatable.
# while game_should_continue:
#     # Generate a random account from the game data

#     # Making account at position B become the next account at position A.
#     account_a = account_b
#     account_b = random.choice(data) # 아하 이렇게하면 글로벌 안써되되네

#     if account_a == account_b:
#         account_b = random.choice(data)

#     # 와 이렇게 하면 되는구나 
#     # 함수안에 return 으로 print 출력문 넣어서 그 함수를 출력해주면 되는군
#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")

#     # Ask user for a guess.
#     input("Who has more followers? Type 'A' or 'B': ").lower()

#     # Clear the screen
#     print("\n" * 20)
#     print(logo)

#     # Check if user is correct.
#     # - Get follower count of each account.
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     # Give user feedback on their guess.
#     # score keeping.
#     if is_correct:
#         score +=1
#         print(f"You're right! Current score {score}")
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}")
#         game_should_continue = False




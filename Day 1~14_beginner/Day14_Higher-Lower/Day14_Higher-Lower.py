# 250920~22 Day 11~13 of Python

# Day 14 Project
# Making the Higher-Lower Game project

import random
from Day14_game_data import data

rand_team = random.choice(data)
rand_club = rand_team['club']
rand_home = rand_team['home']
rand_year = rand_team['previous_winning_year']
rand1_wins = rand_team['wins']

A = print(f"Compare A : {rand_club}, Home: {rand_home}, Previous_winning_year: {rand_year}.\n")

rand_team = random.choice(data)
rand_club = rand_team['club']
rand_home = rand_team['home']
rand_year = rand_team['previous_winning_year']
rand2_wins = rand_team['wins']

B = print(f"Against B : {rand_club}, Home: {rand_home}, Previous_winning_year: {rand_year}.\n")

answer = input("Which team won more? Type 'A' or 'B': ").upper()

score = 0
if answer == 'A':
    if rand1_wins > rand2_wins:
        score += 1
        print(f"You're right! Current score: {score}.\n")
    elif rand1_wins < rand2_wins:
        print(f"Sorry, that's wrong. Final Score: {score}")
    else:
        print(f"Sorry, that's Draw. Current Score: {score}")
elif answer == 'B':
    if rand1_wins < rand2_wins:
        score += 1
        print(f"You're right! Current score: {score}.\n")
    elif rand1_wins > rand2_wins:
        print(f"Sorry, that's wrong. Final Score: {score}")
    else:
        print(f"Sorry, that's Draw. Current Score: {score}")
else:
    print(f"Sorry, that's wrong type. Type 'A' or 'B'. ")
    answer = input("Which team won more? Type 'A' or 'B': ").upper()
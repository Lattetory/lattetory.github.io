# 250917~18 Day 8 ~ 9 of Python

# Day 11 Project
# Making the BlackJack project

logo = '''
.------.         _     _            _    _            _
|A_  _ |.       | |   | |          | |  (_)          | |
|( \\/ ).------. | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  / |K /\\  | | '_ \\| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \\/  | /  \\ | | |_) | | (_| | (__|   <| | (_| | (__|   <
'------| \\  / | |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__._|\\___|_|\\_\\
       |  \\/ K|                        _/ |
       '------'                       |__/
'''

import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def start():
    begin = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if begin == "n":
        print("Good Bye!")
    else:
        print("\n" * 10)
        print(logo)
        restart = True
        user_cards = []
        dealer_cards = []

        def final_hand():
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}\n")

        def deal_card():
            user_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))
            print(f"\nYour cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Dealer's first card: {dealer_cards[0]}\n")
            # 여기서 승패 여부 
            # 승패여부 함수를 따로 뺄까.. 
            # 그래야겠네 keep n 눌렀을때 확인하려면 
            # 결과함수도 승 패 무 이렇게 나눠야되나
        def result():
            if sum(user_cards) > 21:
                final_hand()
                print("You went over. You lose.\n")
                start()
            elif sum(dealer_cards) > 21:
                final_hand()
                print("You Win!")
                start()
            else:
                pass

        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        deal_card()
        result()
        
        # 여긴 카드 더 받고 진행 할건지만
        while restart == True:
            keep = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if keep == "y":
                deal_card()
                result()
                restart = True
            elif keep == "n":
                result()
                restart = False
                print("\n" * 10)
                start()
            else: 
                print(keep)

start()

    # 카드 랜덤 리스트 , 총합 d
    # 딜러카드 첫장만 공개 d
    # 유저 카드 더 뽑을지 d
    # 더 뽑으면 카드 추가, 합산 d
    # 블랙잭이면 무조건 승리
    # 21초과시 유저 패배ㅇ
    # 또는 딜러가 유저보다 낮으면 승리
    # 그만 뽑으면 딜러 카드 공개
    # 딜러는 17이하일 경우 카드 뽑기
    # 딜러가 21초과시 유저 승리
    # 계속 할건지

        
    
    # restart = True

    # while restart == True:
    #     pick_operations()
    #     pick_op = input("Pick an operation: ")
    #     num2 = float(input("What's the next number? : "))
    #     for a in operations:
    #         if a == (pick_op):
    #             answer = operations[pick_op](num1, num2)
    #             print(f"{num1} {pick_op} {num2} = {answer}")
    #     save = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    #     if save == "y":
    #         num1 = answer
    #         restart = True
    #     else:
    #         restart = False
    #         print("\n" * 7)
    #         start()

# if begin == "y":
#     start()




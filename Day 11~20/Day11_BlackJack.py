# 250917~18 Day 8 ~ 9 of Python

# Day 11 Project
# Making the BlackJack project

# 내가 찾은 답!!! 겨우 혼자 했다!! 
# logo = '''
# .------.         _     _            _    _            _
# |A_  _ |.       | |   | |          | |  (_)          | |
# |( \\/ ).------. | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \\  / |K /\\  | | '_ \\| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
# |  \\/  | /  \\ | | |_) | | (_| | (__|   <| | (_| | (__|   <
# '------| \\  / | |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__._|\\___|_|\\_\\
#        |  \\/ K|                        _/ |
#        '------'                       |__/
# '''

# import random

# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# def start():
#     begin = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#     if begin == "n":
#         print("\nGood Bye!\n")
#         restart = False
#         print("\n" * 10)
#         start()
#     else:
#         print("\n" * 10)
#         print(logo)
#         restart = True
#         user_cards = []
#         dealer_cards = []

#         def final_hand():
#             print(f"\nYour final hand: {user_cards}, final score: {sum(user_cards)}")
#             print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}\n")

#         def deal_card():
#             user_cards.append(random.choice(cards))
#             dealer_cards.append(random.choice(cards))
#             A_change()
#             print(f"\nYour cards: {user_cards}, current score: {sum(user_cards)}")
#             print(f"Dealer's first card: {dealer_cards[0]}\n")

#         # A 카드 체인지
#         def A_change():
#             for i in user_cards:
#                 if sum(user_cards) > 21 and i == 11 :
#                     user_cards.remove(i)
#                     user_cards.append(1)
#             for i in dealer_cards:
#                 if sum(dealer_cards) > 21 and i == 11 :
#                     dealer_cards.remove(i)
#                     dealer_cards.append(1)


#         def no_keep_black():
#             # 블랙잭일시 
#             if user_cards == [ 10, 11 ] or user_cards == [ 11, 10 ]:
#                 if dealer_cards == [ 10, 11 ] or dealer_cards == [ 11, 10 ]:
#                     final_hand()
#                     print("Both BlackJack! :) Draw!")
#                     start()
#                 else:
#                     final_hand()
#                     print("BlackJack! :) You win!")
#                     start()
                
#             if dealer_cards == [ 10, 11 ] or dealer_cards == [ 11, 10 ]:
#                 final_hand()
#                 print("BlackJack! :( You lose!")
#                 start()

#         def no_keep_just():
#             # 단순비교시
#             if sum(user_cards) > sum(dealer_cards):
#                 final_hand()
#                 print("You Win!")
#                 start()
#             elif sum(dealer_cards) > sum(user_cards):
#                 final_hand()
#                 print("You went over. You lose.\n")
#                 start()
#             else:
#                 final_hand()
#                 print("Draw.\n")
#                 start()

#     # 이건 21 초과시
#         def result():
#             if sum(user_cards) > 21:
#                 final_hand()
#                 print("You went over. You lose.\n")
#                 start()
#             elif sum(dealer_cards) > 21:
#                 final_hand()
#                 print("You Win!")
#                 start()
#             else:
#                 pass

#         user_cards.append(random.choice(cards))
#         dealer_cards.append(random.choice(cards))
#         deal_card()
#         no_keep_black()
#         result()
        
#         # 여긴 카드 더 받고 진행 할건지만
#         while restart == True:
#             keep = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#             if keep == "y":
#                 deal_card()
#                 result()
#                 restart = True
#             elif keep == "n":
#                 no_keep_black()
#                 no_keep_just()
#                 restart = False
#                 print("\n" * 10)
#                 start()
#             else: 
#                 print(keep)

# start()


# 정답  와.. 이렇게 간단한거였다니.. 
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

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the scor calculated from cards"""
    if sum(cards) == 21 and len(cards) == 2: # 블랙잭 확인
        # if 11 in cards and 10 in cards 
        # 해도 되지만 어차피 2개카드중 21 나오는건 10, 11뿐
        return 0
    
    if 11 in cards and sum(cards) > 21: # A 카드 체인지
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# 점수 비교    허허 이렇게 간단하다니...
# 순서대로 검사하되 리턴으로 빠져나옴
def compare(U_score, C_score):
    if U_score == C_score:
        return "Draw."
    elif C_score == 0:
        return "Lose, opponet has Blackjack! :("
    elif U_score == 0:
        return "Win with a Blackjack! :)"
    elif U_score > 21:
        return "You went over. You lose :("
    elif C_score > 21:
        return "Opponent went over. You win :)"    
    elif U_score > C_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1 # 딜러 17이하 일때 카드 뽑을때 정의 안되어 오류떠서 변수선언
    user_score = -1 # not is_game_over while문 일때 역시나 오류떠서 선언
    is_game_over = False

    for _ in range(2): # _ > 특정 변수가 실제로 필요하지 않기 때문
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 사용자가 계속 카드 받을 수 있도록
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 딜러가 자신의 전략을 따를 수 있도록
    while computer_score != 0 and computer_score < 17: 
        # 아하 나 뽑을때 같이 뽑는게 아니구나 
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}\n")
    print(compare(user_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 15)
    play_game()




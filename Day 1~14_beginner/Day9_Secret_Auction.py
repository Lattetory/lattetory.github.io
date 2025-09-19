# 250916 7일차

# programming_dictionary = {
#     "Latte" : "So Cute",
#     "MoonLatte" : "So Cool",
#     # 이렇게 들여쓰기 
# }

# print(programming_dictionary["Latte"])

# programming_dictionary["TTETTE"] = "latte Nickname" # 딕셔너리 추가

# programming_dictionary = {} # 딕셔너리 초기화 > 게임 종료후 데이터 초기화 할때 사용할수있음

# programming_dictionary["Latte"] = "My Cat" # 밸류값 변경

# print(programming_dictionary)

# loop through a dictionary

# for key in programming_dictionary:
#     print(key) # 이렇게만 하면 키값만 출력됨(꼭 'key'라고 안해도 키값만 출력됨)
#     print(programming_dictionary[key]) # 밸류값 출력

# Quiz

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for student_name in student_scores:
#     if student_scores[student_name] >= 91:
#         student_grades[student_name] = "Outstanding"
#     elif student_scores[student_name] >= 81:
#         student_grades[student_name] = "Exceeds Expectations"    
#     elif student_scores[student_name] >= 71:
#         student_grades[student_name] = "Acceptable" 
#     else :
#         student_grades[student_name] = "Fail" 

# print(student_grades)

# Nesting _ 중복

# capitals = {
#     "Korea": "Seoul",
#     "Germany": "Berlin",
# }

# Neseted List in Dictionary

# travel_log = {
#     "Korea": ["Seoul", "Incheon", "GyungGiDo"], # 이렇게 여러게 넣을려면 리스트나 딕셔너리로 
#     "Germany": ["Stuttgart", "Berlin"]
# }
# # print Incheon
# print(travel_log["Korea"][1]) # list in dictionary 딕셔너리 안 리스트 출력방법

# nested_list = ["A", "B", ["C","D"]]
# # print D
# print(nested_list[2][1]) # 리스트 안 리스트 출력

# travel_log = {
#     "Korea": {
#         "num_times_visited" : 1004, # 딕셔너리 안에 딕셔너리 안에 리스트
#         "cities_visited" : ["Seoul", "Incheon", "GyungGiDo"]
#     },
#     "Germany": {
#         "num_times_visited" : 7,
#         "cities_visited" : ["Stuttgart", "Berlin"]}
# }
# # print GyungGiDo # 딕셔너리 안에 딕셔너리 안에 리스트 출력
# print(travel_log["Korea"]["cities_visited"][2])


# Day 9 Project
# Making the secret auction program

# 내가 찾은 답! > 내것이 더 간단해보이는디...
# logo = '''
#          __________
#          \\        /
#           )______(
#          |""""""""|_.-._,.-------.,_.-.-
#          |        | | |             | | ''_.
#          |        |_| |_           _| |_..='
#          |________| '_' ',_______,'
#          )""""""""(
#         /__________\\
#        .------------.
#       /______________\\

# '''
# print(logo)
# print("Welcome to the secret auction program")
# continue_bidding = False

# members = {}

# while continue_bidding:
#     name = input("What is your name? : ")
#     bid = int(input("What's your bid? : $ "))
#     members[name] = bid
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
#     print("\n" * 20)
#     if should_continue == "no":
#         continue_bidding = True

# winner = {}
# max = 0

# for name in members:
#     if members[name] >= max:
#         max = members[name]
#         winner = name

# print(f"The winner is {winner} with a bid of $ {max}")


# 정답
logo = '''
         __________
         \\        /
          )______(
         |""""""""|_.-._,.-------.,_.-.-
         |        | | |             | | ''_.
         |        |_| |_           _| |_..='
         |________| '_' ',_______,'
         )""""""""(
        /__________\\
       .------------.
      /______________\\

'''
print(logo)
print("Welcome to the secret auction program")
continue_bidding = True

bids = {}


def find_highest_bidder(bidding_dictionary): # bids 딕셔너리
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of $ {highest_bid}")

while continue_bidding:
    name = input("What is your name? : ")
    price = int(input("What's your bid? : $ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids) # bids 딕셔너리 
    else:
        print("\n" * 20)



# 250924 Day 15 of Python

# Day 15 Project
# Making the Coffee Machine project

# print report.
# check resources sufficient?
# process coins.
# check transaction successful?
# Make Coffee.


# 내가 짠 코드! 근데 넘 길당 ㅎ 
# 어쨌든 해결!! 

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1500,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2500,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3000,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# wons = 0

# # 리포트 값 출력 함수
# def report():
#     water = print(f"Water : {resources["water"]}ml")
#     milk = print(f"Milk : {resources["milk"]}ml")
#     coffee = print(f"Coffee : {resources["coffee"]}g")
#     money = print(f"Money : {wons}won")

# run = True

# while run:
#     # 주문받기
#     ordering = True
#     coining = True

#     while ordering:
#         order = input("What would you like? (espresso/latte/cappuccino): ").lower()    # 재료 있는지 확인+ 가능시 재료 소진 + 재료 소진시 불가 안내
                
#         if order == "report":
#             report()
#             ordering = True
            
#         elif order == "espresso":
#             # 일단 재료 빼는건 이건데 하나하나 적어줘야되나.. 흠
#             resources["water"] -= MENU["espresso"]["ingredients"]["water"]
#             resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
#             if resources["water"] < 0:
#                 print(f"Sorry there is not enough water")
#                 ordering = True
#             elif resources["coffee"] < 0:
#                 print(f"Sorry there is not enough coffee")
#                 ordering = True
#             else:
#                 ordering = False

#         elif order == "latte":
#             resources["water"] -= MENU["latte"]["ingredients"]["water"]
#             resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
#             resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
#             if resources["water"] < 0:
#                 print(f"Sorry there is not enough water")
#                 ordering = True
#             elif resources["milk"] < 0:
#                 print(f"Sorry there is not enough milk")
#                 ordering = True
#             elif resources["coffee"] < 0:
#                 print(f"Sorry there is not enough coffee")
#                 ordering = True    
#             else:
#                 ordering = False

#         elif order == "cappuccino":
#             resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
#             resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
#             resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
#             if resources["water"] < 0:
#                 print(f"Sorry there is not enough water")
#                 ordering = True
#             elif resources["milk"] < 0:
#                 print(f"Sorry there is not enough milk")
#                 ordering = True
#             elif resources["coffee"] < 0:
#                 print(f"Sorry there is not enough coffee")
#                 ordering = True    
#             else:
#                 ordering = False

#         elif order == "off":
#             print("Coffee Machine off.")
#             ordering = False
#             coining = False
#             run = False

#         else:
#             print("Sorry. that's wrong order.")
#             ordering = True

#     while coining:
#         # 돈 받기
#         print("Please insert coins.")
#         obackwon = int(input("How many 500won?: ")) * 500
#         backwon = int(input("How many 100won?: ")) * 100
#         osibwon = int(input("How many 50won?: ")) * 50
#         sibkwon = int(input("How many 10won?: ")) * 10
#         won = obackwon+backwon+osibwon+sibkwon

#         # 계산 잔돈 + 음료 주기
#         bill = won - MENU[order]["cost"]
#         if bill < 0:
#             print("Sorry that's not enough money. Money refunded.")
#         else:
#             print(f"Here is {bill}won in change.")
#             print(f"Here is your {order}. Enjoy!")
#             wons += MENU[order]["cost"]
#             coining = False



# 정답

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients): # 재료 비교
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, 
        or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2) # 소수점 두자리
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. :)")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


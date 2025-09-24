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

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1500,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2500,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3000,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

wons = 0

# 리포트 값 출력 함수
def report():
    water = print(f"Water : {resources["water"]}ml")
    milk = print(f"Milk : {resources["milk"]}ml")
    coffee = print(f"Coffee : {resources["coffee"]}g")
    money = print(f"Money : {wons}won")

run = True

while run:
    # 주문받기
    ordering = True
    coining = True

    while ordering:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()    # 재료 있는지 확인+ 가능시 재료 소진 + 재료 소진시 불가 안내
                
        if order == "report":
            report()
            ordering = True
            
        elif order == "espresso":
            # 일단 재료 빼는건 이건데 하나하나 적어줘야되나.. 흠
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            if resources["water"] < 0:
                print(f"Sorry there is not enough water")
                ordering = True
            elif resources["coffee"] < 0:
                print(f"Sorry there is not enough coffee")
                ordering = True
            else:
                ordering = False

        elif order == "latte":
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            if resources["water"] < 0:
                print(f"Sorry there is not enough water")
                ordering = True
            elif resources["milk"] < 0:
                print(f"Sorry there is not enough milk")
                ordering = True
            elif resources["coffee"] < 0:
                print(f"Sorry there is not enough coffee")
                ordering = True    
            else:
                ordering = False

        elif order == "cappuccino":
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            if resources["water"] < 0:
                print(f"Sorry there is not enough water")
                ordering = True
            elif resources["milk"] < 0:
                print(f"Sorry there is not enough milk")
                ordering = True
            elif resources["coffee"] < 0:
                print(f"Sorry there is not enough coffee")
                ordering = True    
            else:
                ordering = False

        elif order == "off":
            print("Coffee Machine off.")
            ordering = False
            coining = False
            run = False

        else:
            print("Sorry. that's wrong order.")
            ordering = True

    while coining:
        # 돈 받기
        print("Please insert coins.")
        obackwon = int(input("How many 500won?: ")) * 500
        backwon = int(input("How many 100won?: ")) * 100
        osibwon = int(input("How many 50won?: ")) * 50
        sibkwon = int(input("How many 10won?: ")) * 10
        won = obackwon+backwon+osibwon+sibkwon

        # 계산 잔돈 + 음료 주기
        bill = won - MENU[order]["cost"]
        if bill < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is {bill}won in change.")
            print(f"Here is your {order}. Enjoy!")
            wons += MENU[order]["cost"]
            coining = False





# 250910 ~ 250911 2일차

# num = int(input("What is the number you want to check? "))
# if num % 2 == 0:
#     print("It's Even Number")
# else:
#     print("It's Odd Number")

# Pizza 
# print("welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L : ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N : ")
# extra_cheese = input("Do you want extra cheese? Y or N : ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print(input("You typed the wrong inputs"))
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is : ${bill}.")


# Day 3 Project
# Making the Treasure Game program

print("""
##################################################################
""")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
cross_road = input('Type "left" or "right"\n').lower()
if cross_road == "right":
    print("You fell in to a hole.")
    print("You're Game Over. Try again.")
else:
    print("You've come to a lake. There is an island in the middle of the lake")
    lake = input('Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if lake == "swim" :
        print("You fell in to a lake.")
        print("You're Game Over. Try again.")
    else:
        print("you've come to the door. Which choice the door?")
        door = input('Type "red". Type "blue". Type "yellow".\n').lower()
        if door != "yellow":
            print("You fell in to a hole.")
            print("You're Game Over. Try again.")
        else:
            print("You're find the treasure box!")
            print("You Win!")
print("""
##################################################################
""")
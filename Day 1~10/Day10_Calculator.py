# 250916 7일차

# # 1
# def format_name():
#     f_name = input("What's your first name?\n").capitalize() # 첫글자를 대문자로 바꿔줌
#     l_name = input("what's your last name?\n").title()      # .title() 로도 할수있음
#     print(f"Your name is {f_name} {l_name}.")               # .lower() 는 모두 소문자

# format_name()

# #2
# def format_name(f_name, l_name):
#     f_name = f_name.capitalize()
#     l_name = l_name.title()      
#     print(f"Your name is {f_name} {l_name}.")   

# format_name(f_name= "laTTe", l_name= "mOoN")

# 3
# def format_name(f_name, l_name):
#     f_name = f_name.capitalize() 
#     l_name = l_name.title()     
#     return f"Your name is {f_name} {l_name}." # return은 출력값이 나오는 함수를 만들기 위해 가장 중요

# print(format_name(f_name= "laTTe", l_name= "mOoN"))           

# print 와 return의 차이점
# return 밑에는 절대 실행되지않음 > 즉, 함수 종료

# def format_name(f_name, l_name):
# # Dcostrings > 꼭 첫줄에 써야함 큰따옴표 3개 내가 만든 함수 설명
#     """Take a first and last name and format 
#     it to return the title case version of the name. """
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs" # 조기 리턴
#     formated_f_name = f_name.title() 
#     formated_l_name = l_name.title()     
#     return f"Result: {formated_f_name}, {formated_l_name}"              

# print(format_name(input("What's your first name?\n"), input("what's your last name?\n")))

# Quiz _ 윤년
# 주어진 연도가 윤년인지 아닌지를 반환하는 프로그램을 작성하세요. 
# 결과는 True 또는 False여야 합니다.

# 특정 연도가 윤년인지 확인하는 방법입니다.
# - 나머지가 없이 4로 나누어 떨어지는 모든 해에 해당합니다.
# -> 나머지가 없이 100으로 나누어 떨어지는 모든 해를 제외합니다. > 즉, 나머지있으면 윤년?
# -> 해당 연도가 400으로 나누어 떨어지는 경우는 제외합니다.

# 예. 2000년:
# 2000 ÷ 4 = 500 (Leap)  
# 2000 ÷ 100 = 20 (Not Leap)  여기서 이미 윤년이라는건가?
# 2000 ÷ 400 = 5 (Leap!)  
# 따라서 2000년은 윤년입니다.

# 그러나 2100년은 윤년이 아닙니다. 왜냐하면:
# 2100 ÷ 4 = 525 (Leap)  
# 2100 ÷ 100 = 21 (Not Leap)  아니어서 한번더 실행?
# 2100 ÷ 400 = 5.25 (Not Leap)  뭐라는겨;ㅋ;

# 쩝 ; 윤년 계산방식이 몬소린지 모르겠다

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# print(is_leap_year(1989))



# Day 10 Project
# Making the Calculator program

# Todo-1: Write out the other 3 functions - subtract, multiply, divide.
# Todo-2: Add these 4 functions into a dictionary as the values. keys = "+", "-", "*", "/"
# Todo-3: Use the dictionary operations to perform the calculations. Multiply 4 * 8

logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |
| |_________________| |
|  --- --- ---   ---  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
|  --- --- ---   ---  |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
|  --- --- ---   ---  |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
|  --- --- ---   ---  |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add, 
    "-" : subtract, 
    "*" : multiply, 
    "/" : divide
    } # print(operations["*"](4, 8))

def pick_operations():
    print("+\n-\n*\n/")

def start():
    print(logo)
    num1 = float(input("What's the first number? : "))
    restart = True

    while restart == True:
        pick_operations()
        pick_op = input("Pick an operation: ")
        num2 = float(input("What's the next number? : "))
        for a in operations:
            if a == (pick_op):
                answer = operations[pick_op](num1, num2)
                print(f"{num1} {pick_op} {num2} = {answer}")
        save = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if save == "y":
            num1 = answer
            restart = True
        else:
            restart = False
            print("\n" * 7)
            start()

start()

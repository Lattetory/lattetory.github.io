# 251106 Day 58 of Python

# Day 26 Project
# Working with CSV Files and Analysing Data with Pandas
# + List Comprehension


import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day15~30_intermediate\Day25_Guess_City_name\Day25_Guess_city_name\\blank_states_img.gif" # 경로
screen.addshape(image) # turtle shape 에 이미지 추가
turtle.shape(image) # 위에 추가해서 지정할 수 있게 됨
data = pandas.read_csv("Day15~30_intermediate\Day25_Guess_City_name\Day25_Guess_city_name\\50_states.csv")

all_states = data.state.to_list() # 리스트 형태로 만들어두기 > 추측과 비교하기 위해
guessed_states = [] # 루프 돌려주기 위해, 정답갯수도

while len(guessed_states) < 50: 

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [] 
        for state in all_states: # 못맞춘 주들 
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day15~30_intermediate\Day26_NATO_Alphabet\Day26_better_Guess_city_name\\states_to_learn.csv")
        break
    if answer_state in all_states: 
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] 
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) # state_data.state.item() 도 되지만 저게 더 간단함
        

















# 각 주의 좌표 값 얻기
# def get_mouse_click_coor(x, y): # 마우스 클릭하는 위치의 x, y 좌표 전달
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor) # 이벤트 리스너 마우스 클릭하면 이 함수 호출
# 이렇게 각 주의 좌표를 얻을 수 있지만
# 적어논 CSV 파일로 진행~!



# turtle.mainloop() # 코드가 실행을 끝내도 화면이 계속 열려있도록 해줌
# 정답에 Exit 입력시 break 문으로 끝낼 수 있도록 해놔서 없앰 



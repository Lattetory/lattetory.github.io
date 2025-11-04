# 251104, 05 Day 56, 57 of Python

# Day 25 Project
# Working with CSV Files and Analysing Data with Pandas

import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day15~30_intermediate\Day25_Guess_City_name\Day25_Guess_city_name\\blank_states_img.gif" # 경로
screen.addshape(image) # turtle shape 에 이미지 추가

turtle.shape(image) # 위에 추가해서 지정할 수 있게 됨

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

# 1. Convert the guess to Title case
# 2. Check if the guess is among the 50 states
# 3. Write correct guesses onto the map
# 4. Use a loop to allow the use to keep guessing
# 5. Record the correct guesses in a list
# 6. Keep track of the score

# 1. 추측을 제목 케이스로 변환합니다
# 2. 추측이 50개 주 중 하나인지 확인합니다
# 3. 지도에 정확한 추측을 작성하기
# 4. 루프를 사용하여 계속 추측할 수 있도록 합니다
# 5. 목록에 올바른 추측을 기록하세요
# 6. 점수 추적하기









# 각 주의 좌표 값 얻기
# def get_mouse_click_coor(x, y): # 마우스 클릭하는 위치의 x, y 좌표 전달
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor) # 이벤트 리스너 마우스 클릭하면 이 함수 호출
# 이렇게 각 주의 좌표를 얻을 수 있지만
# 적어논 CSV 파일로 진행~!



turtle.mainloop() # 코드가 실행을 끝내도 화면이 계속 열려있도록 해줌
















# 250913 4일차

# Day 6 Project
# Making the Maze escape program

# 15일차 강의까지 수료 후 다시 돌아와서 디버깅 중급 문제 해결해보기!
# 11분 47초
# 3개의 오류 파일 불러서 오류 없는지 확인하기
# 단계가 1000개 이하면 성공!

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# 내가 찾은 답 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
        
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
    
# while not at_goal():
#     if wall_in_front():
#         turn_left()
#     elif right_is_clear():
#         if not wall_in_front():
#             move()
#         else:
#             turn_right()
#     else:
#         jump()

# 정답 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
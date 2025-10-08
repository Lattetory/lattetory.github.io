# 251008 Day 29 of Python

# # from turtle import Turtle, Screen
# import turtle as t
# import random
# # 터틀 프로그램에 자세한 사용설명은 구글에 찾아보면됨 ㅋㅎ
# # https://docs.python.org/3/library/turtle.html
# # from turtle import * # * 은 모든 것을 뜻함
# # 하지만 어디서 왔는지 파악하기 어렵기때문에 쓰이지않음
# # import turtle as t # 라고 하면
# # tim = turtle.Turtle() > tim = t.Turtle() 로 줄일수있음

# tim = t.Turtle() # 이렇게만 하면 바로 사라지기 때문에
# tim.shape("turtle")
# tim.color("DarkGoldenrod2")
# # tim.forward(100)
# # tim.right(45)


# # 정사각형 그리기
# # for i in range(4):
# #     tim.forward(100)
# #     tim.right(90)

# # 실선 그리기
# # for i in range(15):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()

# # 여러 도형 그리기
# # colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple", "pink"]
# # a = 3
# # angle = 360
# # while a < 11:
# #     for i in range(a): 
# #         tim.color(colors[a-3])
# #         tim.forward(100)
# #         tim.right(angle/a)
# #     a += 1

# # 정답
# # def draw_shape(num_sides):
# #     angle = 360 / num_sides
# #     for _ in range(num_sides):
# #         tim.forward(100)
# #         tim.right(angle)

# # for shape_side_n in range(3, 11):
# #     tim.color(random.choice(colors))
# #     draw_shape(shape_side_n)

# # 무작위 행보
# # def draw_shape(dir):
# #     angle = 90 * random.randint(1,5)
# #     tim.pensize(10)
# #     tim.speed(50)
# #     tim.right(angle)
# #     tim.forward(30)

# # for shape_side_n in range(100):
# #     tim.color(random.choice(colors))
# #     draw_shape(shape_side_n)

# # 정답
# dir = [0, 90, 180, 270]

# t.colormode(255)

# def random_color(): # 지정된색 아닌 rgb 랜덤
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# # for shape_side_n in range(200):
# #     tim.pencolor(random_color()) # 지정된색 아닌 rgb 랜덤
# #     tim.pensize(15)
# #     tim.speed("fastest")
# #     tim.setheading(random.choice(dir))
# #     tim.forward(30)


# # Make a Spirograph
# # for _ in range(100):
# #     tim.speed("fastest")
# #     tim.pencolor(random_color())
# #     tim.circle(120)
# #     tim.left(3.6)

# # 정답
# def draw_spirograph(size_of_gap): # 원들의 간격 
#     for _ in range(int(360 / size_of_gap)):
#         tim.speed("fastest")
#         tim.pencolor(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5) # 5만큼의 간격


# screen = t.Screen()
# screen.exitonclick() # 클릭하면 사라지도록 설정_ 맨아래로 이동


# colorgram package > 이미지 컬러 추출!
# 난 지금 안할거지만 나중에 쓰일수있기에 방법 그대로 적어두기!

# # import colorgram
# # rgb_colors = []
# # colors = colorgram.extract('image.jpg', 30)
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     new_color = (r, g, b)
# #     rgb_colors.append(new_color)
# # print(rgb_colors) # 로 출력해서 나온 값 복사해서

# color_list = [(어쩌구),(저쩌구)] # 붙여넣기 하고 윗 코드들 주석처리



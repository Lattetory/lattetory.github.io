# weather_data

# with open("Day15~30_intermediate\Day25_Guess_City_name\Day25_CSV_Pandas\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# 이렇게만 하면 , 로 구분되어있는 리스트 나옴

# import csv

# with open("Day15~30_intermediate\Day25_Guess_City_name\Day25_CSV_Pandas\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data: # 이렇게 하면 각 요소들은 하나의 값으로 분리되어 있음
#         if row[1] != "temp":
#             temperatures.append(int(row[1])) # int 안하면 문자열로 됨 
#     print(temperatures)

# 를 보다 편하게 쓰기위해 Pandas 이용!
# 정말 표처럼 보이게 해줌(선이 있다기보단 정렬정도?)

import pandas

data = pandas.read_csv("Day15~30_intermediate\Day25_Guess_City_name\Day25_CSV_Pandas\weather_data.csv")
# pandas 에는 두가지 주요 데이터 구조 있음
# 1. series(한개의 열) 2. dataframe(전체)
# print(type(data)) # DataFrame 유형 (전체 표와 같은 것)
# print(type(data["temp"])) # series 유형 (1차원 데이터 배열인 것(즉 한개의 열 ex_요일 열, 온도 열, 날씨 열)
# 첫줄을 제목처럼 했기에 temp 열 쭈루룩 나옴
# 하면 위 import csv 처럼 temp 값만 나오되 표처럼 나옴

# print(data)

# data_dict = data.to_dict() # 딕셔너리 형태로 나옴
# print(data_dict)

# temp_list = data["temp"].to_list() # 파이썬 리스트 형태로 
# print(temp_list)


# 평균 온도 계산해보기

# temp = 0
# for i in temp_list:
#     temp += i
# avg_temp = temp/len(temp_list)

# 허허허.. sum 이 있었네.. 젠장 ㅋㅋ
# average = sum(temp_list)/len(temp_list)
# print(average)
# 를 또 줄여서 

# print(data["temp"].mean()) # 한줄 메소드로 완성 / .mean() 평균값구하기


# 최고, 최저값 찾기

# high_temp = data["temp"].max() # data.temp.max() 라고 써도 됨
# # print(high_temp)
# print(data["temp"].min())


# Get Data in Columns(열)

# print(data["condition"]) 
# print(data.condition)
# 두개다 같은 값 불러옴

# Get Data in Row(행)

# print(data[data.day == "Monday"])


# 가장 높은 온도 데이터가 있는 행 추출하기

# print(data[data.temp == data.temp.max()]) # data[data.temp == high_temp]


# 특정 요일에 대한 날씨

# monday = data[data.day == "Monday"] 
# print(monday.condition)


# 월요일 온도 추출인데 섭씨에서 화씨로 바꾸기 / 공식 온도 * 1.8 + 32

# print((monday.temp) * 1.8 + 32)
# 도 되지만 값만 얻고싶을땐
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32 # 이 공식도 맞나봄
# print(monday_temp_F)


# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# 이 딕셔너리에서 데이터프레임 얻기 / 즉, 파이썬에서 판다스 표로 만들기 가능
data_1 = pandas.DataFrame(data_dict)
print(data_1)

# 이 데이터프레임으로 CSV 로 변환도 가능!
data_1.to_csv("Day15~30_intermediate\Day25_Guess_City_name\Day25_CSV_Pandas\\new_data.csv") # 괄호안에는 파일 만들어질 경로


# 워후 뭐 다람쥐 어쩌구 있는데 이건 보기만 할게영.. 
# 오픈소스 받고 어쩌고 너무 많당
# 그냥 코드만 따라 적어봄

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squireel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
# df = pandas.DataFrame(data_dict) # 초기화 해줘야함
# df.to_csv("squirrels_count.csv") # 경로 정해야하는데 나는 저장 안하니까 그냥 이렇게만 씀








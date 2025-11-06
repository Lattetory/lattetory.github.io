# 251106 Day 58 of Python

# Day 26 Project
# Dictionary Comprehension
# Pandas DataFrame roop

# 딕셔너리 만드는 방법
# new_dict = {'new_key':'new_value' for 'item' in 'list'}

# 기존 딕셔너리 값을 가지고 새로운 딕셔너리 만드는 방법
# new_dict = {'new_key':'new_value' for '(key,value)' in 'dict.items()' if 'test'}

# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_scores = {student:random.randint(1, 100) for student in names}

# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

# print(students_scores)
# print(passed_students)


# # 각 단어의 글자 수 딕셔너리 만들기
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}

# print(result)


# # 섭씨를 화씨로 바꾼 딕셔너리 만들기
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:(int(temp)* 9/5)+32 for (day,temp) in weather_c.items()}

# print(weather_f)


# 판다스 데이터프레임에서 반복문 사용하는 방법, 판다스 데이터프레임을 반복하는 방법
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
## Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

# 판다스 이용하여 표로 바꿈
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

## Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
# 오와 신기해 ㅋㅋ


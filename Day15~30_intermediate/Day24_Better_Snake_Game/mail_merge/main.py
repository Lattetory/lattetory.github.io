# 251103, 04 Day 55, 56 of Python

# Day 24 Project
# Making the mail merge project
# Local Files and Directories


# Todo : Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint 1 : This method will help you: http://www.w3schools.com/python/ref_file_readlines.asp
# Hint 2 : This method will also help you: http://www.w3schools.com/python/ref_string_replace.asp
# Hint 3 : This method will help you : http://www.w3schools.com/python/ref_string_strip.asp


# 상대 경로 / 절대 경로

# 절대 경로 
# 항상 /(슬래시) 로 시작 or  C: or D: 로 시작하는 경로

# 상대 경로
# ./ (점슬래시) 는 현재 폴더를 의미
# .. (점 두개)는 한단계 위 폴더


# 내용 불러오기
startletter = open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Input/Letters/starting_letter.txt", "r")
line = startletter.readlines()
dearname = line[0]
# 이름 불러오기
invitedname = open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Input/Names/invited_name.txt", "r")
lines = 0
names = invitedname.readlines(lines + 1)
name = names[0].strip("\n") # 이름 

# for i in range(7):
#     names = invitedname.readlines(lines + 1)
#     print(names)
#     lines += 1
#     print(changename)
# changename = dearname.replace("[name]", names)
# print(changename)

# 이름 바꾸기
changename = dearname.replace("[name]", name)

print(changename)

# 문장안에 이름 어케바꾸지


# with open(f"/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/{name}].txt", mode= "w") as file:
#     file.write("new file.")








# # 문자열 바꾸기
# names = "I like bananas"

# x = names.replace("bananas", "apples")

# print(x)

# # 문자열 공백 제거 / strip()은 앞뒤의 공백을 제거
# txt2 = "     banana     "

# x = txt2.strip()

# print("of all fruits", x, "is my favorite")

# txt1 = ",,,,,rrttgg.....banana....rrr"

# x = txt1.strip(",.grt")

# print(x)
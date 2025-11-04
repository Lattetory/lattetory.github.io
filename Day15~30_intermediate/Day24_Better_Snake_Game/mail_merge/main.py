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

# 내가 찾은 답!
# 길긴 하지만 혼자 해냈다는게 멋지군
# # 편지 불러오기
# with open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Input/Letters/starting_letter.txt") as letter_file:
#     letter = letter_file.read()
# # print(letter)

# # 이름 불러오기
# line = 0

# # 반복하기
# for i in range(7):

#     # print(line)
#     with open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Input/Names/invited_name.txt") as names_file:
#         names = names_file.readlines()
#     print(names[line])
#     # print(line)


#     # 이름 바꿔넣기
#     changename = letter.replace("[name]", names[line].strip("\n"))

#     print(changename)

#     # 저장하기
#     with open(f"/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Output/ReadyToSend/letter_for_{names[line].strip("\n")}.txt", mode= "w") as letter_for_file:
#         letter_for = letter_for_file.write(changename)
    
#     line += 1

# 왓쉬 만들어따 대박


# 정답

PLACEHOLDER = "[name]"

with open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Input/Names/invited_name.txt") as names_file:
        names = names_file.readlines()

with open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/mail_merge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode= "w") as completed_letter:
            completed_letter.write(new_letter)

# 와 짱 간단하다니..




# 위 힌트 링크들 관련 

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
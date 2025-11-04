# 251015,19 Day 36,40 of Python

# Day 24 Project
# Making the better snake game project
# Local Files and Directories
# https://docs.python.org/3/library/turtle.html
# 만들었던 뱀게임 수정하기

# file = open("my_file.txt")

# contents = file.read()

# print(contents)

# file.close()

# 음.. 난 왜 안되징;;
# 여튼 이렇게 open 하고 close 하는 대신 (close 잘 까먹게 된다함)

with open("/Udemy/Python_bootcamp/Day15~30_intermediate/Day24_Better_Snake_Game/new_file.txt", mode= "w") as file:
    file.write("new file.")

# 이렇게 할 수도 있다 하나 역시나 난 왜 안열리냐;
# 음. 새로 파일 만들어진건 상위폴더에 만들어진다 
# 거기에 만들어야되는건가 여튼 넘어감

# 오!! 경로 써진것처럼 써야 되는구나 ~ 
# 그냥 new_file.txt 만 쓰면 /Udemy/Python_bootcamp 파일에 만들어짐!
# 줄여서 ../../ 이런식으로 쓸수있음!
# 근데 모르겠다 
# 강의에선 /Users/angela/Desktop/my_file.txt 를 줄여서
# ../../Desktop/my_file.txt 로 썼는데
# 나는 왜 안대냥


# read() = 읽기 / "a"
# write() = 쓰기 / "w" / 전에껀 초기화됨
# append() = 추가 / "a" / 전에꺼 + 추가
# 만약 파일이 없다면 새로 만들기도 가능 (위 코드처럼) 실행하면 생김
# write 모드일때만 가능!


# 상대 경로 / 절대 경로

# 절대 경로 
# 항상 /(슬래시) 로 시작 or  C: or D: 로 시작하는 경로

# 상대 경로
# ./ (점슬래시) 는 현재 폴더를 의미
# .. (점 두개)는 한단계 위 폴더

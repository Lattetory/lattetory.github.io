# 251008 Day 29 of Python

# Day 17 Project
# Making the OX Quiz Game project

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # 0은 기본값이기에 위에 안적어도됨
        self.following = 0
        # print("객체 만들어지는 중...")

    def follow(self, user): # 일반 함수와 다르게 첫 매개변수로 self 있어야함
        user.followers += 1
        self.following += 1 # self 와 user객체 구분 잘해야함


user1 = User("001", "latte")
# user1.id = "001"
# user1.username = "latte"
# print(user1.id)
# print(user1.username) 
# print(user1.followers) # 0 기본값출력보려고

user2 = User("002", "tol")
# user2.id = "002"
# user2.username = "tol"
# print(user2.username)

user1.follow(user2)
print(user1.followers) # 0
print(user1.following) # 1 # user1의 following +1 
print(user2.followers) # 1 # user2의 followers +1 
print(user2.following) # 0


# >> 그래서 __init__ 생성자! 
# 객체가 생성됐을때 어떤 것을 해야하는지 명시해줌
# 객체가 생성될때마다 init 함수 호출됨!







# 251011 Day 32 of Python

# Day 21 Project
# Making the Snake Game 2 project
# https://docs.python.org/3/library/turtle.html

# Class Inheritance 클래스 상속

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
    
class Fish(Animal): # 부모클래스 상속 받고싶으면 괄호 안에 넣어주면 됨
    def __init__(self):
        super().__init__() # super = 부모클래스

    def breathe(self):
        super().breathe() # 부모의 함수를 받지만
        print("doing this underwater.") # 이렇게 수정도 가능

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
# 251106 Day 58 of Python

# Day 26 Project
# Making the NATO Alphabet project

# {new_key:new_value for (index, row) in df.iterrows()} 
# interrow() 행을 반복할 수 있게 해주는 메소드, 튜플형태로 반환

# Todo 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Todo 2. Create a list of the phonetic code words from a word that the user iuputs.
# Enter a word: Thomas
# ['Tango', 'Hotel', 'Oscar', 'Mike', 'Alfa', 'Sierra']


import pandas

data = pandas.read_csv("Day15~30_intermediate\Day26_NATO_Alphabet\Day26_NATO_Alphabet\\nato_phonetic_alphabet.csv")

# 내가 찾은 답! 
# word = [alpha for alpha in input("Enter a word: ").upper()]
# answer = []
# for alpha in word:

#     for (index, row) in data.iterrows():
#         if row.letter == alpha:
#             answer += [row.code]

# print(answer)
# 하긴 했는데 몬가 더 줄일 수 있을거같다ㅎㅎ 

# 정답!
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]

print(output_list)

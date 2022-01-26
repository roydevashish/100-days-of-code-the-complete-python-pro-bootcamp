# Day 026
# List and Dictionary Comprehensions
# new_list = [new_item for item in list]

# num = [1, 2, 3]
# new_num = [n+1 for n in num]
# print(new_num)

# name = input("You Name: ")
# name_list = [letter for letter in name]
# print(name_list)

# range(1, 5)
# new_num = [num for num in range(1,5)]
# print(new_num)

# Conditional List Comprehensions
# new_list = [new_item for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_name = [name.upper() for name in names if len(name) < 5]
# print(short_name)

# Squared Numbers using List Comprehensions
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num*num for num in numbers]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)


# Use list comprehension to create a new list called result.
# This new list should only contain the even numbers from the list number.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num%2 == 0]
# print(result)


# Compairing two list using list comprehension

# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
#     file1_list = [int(num) for num in file1_data]
#     file1_set = set(file1_list)

# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
#     file2_list = [int(num) for num in file2_data]
#     file2_set = set(file2_list)   

# result = file1_set.intersection(file2_set)
# result = list(result)
# result = [num for num in file1_list if num in file2_list]
# print(result)

# Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dictionary.item() }

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_list = sentence.split()
# result = {word:len(word) for word in word_list}
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# result = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(result)


# Loop through Pandas Data Frame
import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# print(student_dict)

# student_df = pandas.DataFrame(student_dict)

# print(student_df)
# for (key, value) in student_df.items():
#     print(value)

# for (index, row) in student_df.iterrows():
#     if row.student == "Angela":
#         print(row.score)

# NATO Alphabet Project

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter a word: ").upper()
output = [dictionary[letter] for letter in word]
print(output)
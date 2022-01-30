# FileNotFound
# with open("test.txt", "r") as a_file:
#     a_file.read()

# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_key"]

# IndexError
# a_list = ["a", "b", "c"]
# value = a_list[3]

# TypeError
# text = "abc"
# print(text + 4)

# try:
#     file = open("test.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("test.txt", "w")
#     file.write("new file created.")
# except KeyError as error_message:
#     print(f"{error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed.")


# Raise custome errors
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

# IndexError Handling
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")

# make_pie(4)

# KeyError Handling
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'shares': 21},
#     {'Likes': 33, 'Comments': 8, 'shares': 3},
#     {'Comments': 4, 'shares': 2},
#     {'Comments': 1, 'shares': 1},
#     {'Likes': 19, 'Comments': 3},
# ]

# total_likes = 0

# for post in facebook_posts:
#     try :
#         post["Likes"]
#     except KeyError:
#         post["Likes"] = 0
#     else:
#         total_likes = total_likes + post["Likes"]

# print(total_likes)

# NATO Phonetic Alphabet with KeyError Exception Handling
# import pandas
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output = [dictionary[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(output)

# generate_phonetic()
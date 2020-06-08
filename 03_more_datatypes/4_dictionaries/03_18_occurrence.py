'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''


user_input = input("please enter a word: ")
user_char = list(user_input)

result ={}

for key in user_char:
    result[key]=user_char.count(key)

print("result ="+ str(result))


'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
'''user_input = input("please enter a string of word :)'''

user_input = input("please enter a string: ")
userinput_list = user_input.split()
'''print(userinput_list)'''
output_list =[]

for i in userinput_list:
    output_list.append((tuple(i)))


print("result_list  = " + str(output_list))

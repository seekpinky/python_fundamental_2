'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
'''
input_list = input("please enter a list: ")

list_ = input_list.split()
'''
unique_list = []
dup_list = []
for i in list_:
    count = list_.count(i)
    print(count)
    if count == 1:
        unique_list.append(i)

print(unique_list)
print(dup_list)




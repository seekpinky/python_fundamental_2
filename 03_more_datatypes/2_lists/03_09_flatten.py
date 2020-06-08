'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

for person in people:
    to_print = ""
    for name in person:
        to_print += name + " "
    print(to_print)

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
new_list =[]
print(type(new_list))
for element in starting_list:
    'new_list ='
    print(element)
    for element_2 in element:
        new_list.append(element_2)
        'new_list += str(element_2) +", "'
    print(new_list)

'final_list= new_list.pop()'

'print("[" + final_list + "]")'
print("[" + new_list + "]")
print(type(new_list))



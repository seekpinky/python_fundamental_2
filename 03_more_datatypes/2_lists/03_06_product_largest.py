'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
input_string = input("Enter a list of 10 numbers or elements separated by space: ")
input_list = input_string.split()
max = 0
for i in input_list:
    if int(i) > max:
        max = int(i)
    else:
        max = max

print("the largest number in this list is  " + str(max))








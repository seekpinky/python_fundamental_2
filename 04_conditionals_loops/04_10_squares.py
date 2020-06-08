'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''

output_list=[]

for i in range (1,51):
    output_list.append(i*i)

print("the squares of number from 1 -50: " + str(output_list))


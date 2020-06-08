'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
lower_num = int(input("please enter the lower bound of the sequence :"))
upper_num = int(input("please enter the upper bound of the sequence :"))
total_num = 0
for i in range(lower_num,upper_num+1,1):
    total_num += i


print(total_num)
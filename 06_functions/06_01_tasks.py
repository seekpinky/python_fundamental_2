'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

input_num = int(input("please enter a number between 1 and 1,000,000,000 :"))
test_1 = None
test_2 = None
def four_or_seven_divisible (input_num):
    if input_num % 4 == 0 or input_num % 7 ==0:
        result = True
    else:
        result = False
    return result
def four_and_seven_divisible (input_num):
    if input_num % 4 ==0 and input_num % 7 == 0:
        result = True
    else:
        result = False
    return result

test_1 = four_or_seven_divisible(input_num)
test_2 = four_and_seven_divisible(input_num)
print(f"input number {input_num} is divisible by 4 or 7 : {test_1}")
print(f"input number {input_num} is divisible by 4 and 7 : {test_2}")
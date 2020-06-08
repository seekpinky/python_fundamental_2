'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

running = True

while running:
    num = int ( input("please enter a number between 1 and 1,000,000 ;"))
    if num < 1:
        print("try a bigger number")
    elif num > 10000000:
        print (" try a smaller number")
    else:
        if(num % 3 == 0):
            print(str(num) +"  is divisible by 3 ")
        else:
            print(str(num) + " is not divisible by 3 ")

        running = False

else:
    print(" while loop is over")



print("done")
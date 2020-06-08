'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

input_num = int(input("please enter a number between 0 and 1,000,000,000: "))
guess = 0
difference = input_num-guess
if input_num >=0 & input_num <=1000000:
    while difference > 0:
        guess +=1
        difference = input_num-guess
        if difference ==0:
            break


    else:
        print("the number is" + str(input_num))

    print("the number is:" + str(guess))


else:
    print ("please enter a number between 0 and 1,000,000,000")
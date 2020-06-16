'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
import random

user_input = int(input("Please enter a number 0-2 while 0 = scissor, 1 = rock, 2 = paper : "))
if user_input != 0 and user_input != 1 and user_input != 2:
    print("Please enter a number 0-2 ")

computer_input = random.randint(0,2)
#computer_input = 2

def determine_winner():
    def get_hand(hand):
        output = None
        if hand == 0:
            output = "scissor"
        elif hand == 1:
            output = "rock"
        elif hand == 2:
            output = "paper"
        else:
            output = "wrong number"
        return output

    def winner (user, computer):
        result = None
        if user == 0 and computer == 0:
            result = "Draw "
        elif user == 1 and computer == 1:
            result = "Draw"
        elif user == 2 and computer == 2:
            result = "Draw"
        elif user == 0 and computer == 1:
            result = "User loss"
        elif user == 0 and computer == 2:
            result = "User Win"
        elif user == 1 and computer == 0:
            result = "User win"
        elif user == 1 and computer == 2:
            result = "User loss"
        elif user == 2 and computer == 0:
            result = " User loss"
        elif user == 2 and computer == 1:
            result = "User win"
        return result


    user_hand = get_hand(user_input)
    computer_hand = get_hand(computer_input)
    out_come = winner(user_input, computer_input)

    print(f"computer hand is {computer_hand}, user hand is {user_hand}, result is {out_come} ")

determine_winner()


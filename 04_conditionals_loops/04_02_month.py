'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

first = (input("please enter a number from 1-12 or other"))

if first.isdigit() == True:
    second = int(first)
    if second ==1:
        print("January")
    elif second ==2:
        print("February")
    elif second ==3:
        print("March")
    elif second ==4:
        print("April")
    elif second == 5:
        print("May")
    elif second == 6:
        print("June")
    elif second == 7:
        print("July")
    elif second == 8:
        print("August")
    elif second == 9:
        print("September")
    elif second == 10:
        print("October")
    elif second == 11:
        print("November")
    elif second == 12:
        print("December")
    else:
        print(" Try number 1 to 12. Only 12 months in a year")
else:
    print("Other")


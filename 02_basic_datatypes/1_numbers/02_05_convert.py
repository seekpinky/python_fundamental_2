'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
Int_num = int(input("please enter an interger number") )
Flo_num = float(input ("please enter a float number"))

floor_division = Flo_num//Int_num
multi = Flo_num * Int_num

print("floor division of " + str(Flo_num) + "/" + str(Int_num) +" is " + str(floor_division))
print("multiplicayion of "+ str(Flo_num) + "*" + str(Int_num) + " is "+ str(multi))

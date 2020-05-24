'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = float(input("please enter an investment amount: "))
rate = float(input("please enter an interest rate ( in percentage form) : "))/100
time = float(input("please enter number of years to invest: "))

fut_value = amount*(1+(rate*time))
print("future value is " + str(fut_value))

'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
input_string = input("Enter a list numbers or elements separated by space: ")
input_list = input_string.split()
count = 0
new_list = ''
for i in range(input_list):
    if i % 2 == 0:
        print("odd")
    else:
        print("even")











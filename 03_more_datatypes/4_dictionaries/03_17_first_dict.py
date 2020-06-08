'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
input_int = int(input("please enter an integer: "))
out_dict = {}
for x in range(input_int+1):
    out_dict[x] = x*x

print ("result =" + str(out_dict))
print(type(out_dict))

'''squares = {x: x*x for x in range(6)}

print(squares)'''
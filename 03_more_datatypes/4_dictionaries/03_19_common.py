'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
result = {}

print(dict_1.keys())
print(dict_2.keys())


for i in dict_1.keys():
    for j in dict_2.keys():
        if i ==j:
            print(str(i) + " is the common key")
            result[i] = dict_1.get(i)+dict_2.get(j)
            print(result[i])
            break
'''
        else:
            result[i] = dict_1.get(i)
            print(result.items())
            result[j] = dict_2.get(j)
            print(result.items())
            
'''
'''
for i in dict_1.keys():
    for j in dict_2.keys():
        if i !=j:
            print(str(i) + " is the different key")
            result[i] = dict_1.get(i)+dict_2.get(j)
            print(result[i])
            break
'''


dict_1.update(dict_2)
(dict_1.update(result))
print("result " + str(dict_1))
'''sorted_result = sorted(result.items())
print(sorted_result)
'''






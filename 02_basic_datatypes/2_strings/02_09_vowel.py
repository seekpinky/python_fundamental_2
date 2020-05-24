'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
#enter a sentence
sentence=input("please enter a sentence: ")
#declataion of vowels

vowel_a = "a"
vowel_e = "e"
vowel_i = "i"
vowel_o = "o"
vowel_u = "u"

#occurance of a word using count method
count_a = sentence.count(vowel_a)
count_e = sentence.count(vowel_e)
count_i = sentence.count(vowel_i)
count_o = sentence.count(vowel_o)
count_u = sentence.count(vowel_u)

print("Count of a : " + str(count_a))
print("Count of e : " + str(count_e))
print("Count of i : " + str(count_i))
print("Count of o : " + str(count_o))
print("Count of u : " + str(count_u))

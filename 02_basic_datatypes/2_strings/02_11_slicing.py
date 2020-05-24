'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

word = input("please enter a word :")
#slice the first letter
first=slice(1)
#get the rest of the word
rest=word[1:]
#add the rest of the word and first letter to the end followed by ay
final=rest+word[first]+"ay"

print(final)

'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
# get input sentence
sentence=input("please enter a sentence: ")
# get imput symbol
symbol=input("please enter a symbol: ")
# get first letter
first = sentence[0]
# replace letter w symbol using replace method
sentence.replace(first,symbol)
print(sentence.replace(first,symbol))





'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():

  ''' define the function here'''
  def stat_max (input_list):
    maximum = 0
    for i in input_list:
      if i > maximum:
        maximum = i
    print (f" maximum of the list is : {maximum}")

  def stat_min(input_list):
    minimum = None
    for i in input_list:
      if not minimum:
        minimum = i
      elif i < minimum:
        minimum = i
    print (f" minimum of the list is : {minimum}")



  def stat_avg(input_list):
    sum = 0
    result = 0

    for i in input_list:
      sum +=i

    result = sum / len(input_list)
    print( f" average of the list is : {result}")

  def stat_sum(input_list):
    sum = 0

    for i in input_list:
      sum +=i

    print( f" sum of the list is : {sum}")

  stat_max(example_list)
  stat_min(example_list)
  stat_avg(example_list)
  stat_sum(example_list)


  pass

# call the function below here
stats()
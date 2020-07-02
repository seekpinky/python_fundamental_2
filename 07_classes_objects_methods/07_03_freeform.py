'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class AmericanFootball:
  league_type ="NFL"
  sport_type = "American Football"
  def __init__(self,team,payroll=0):
    self.team = team
    self.payroll= payroll
  def __str__(self):
    return(" team: {rank1} payroll: {rank2}".format(rank1=self.team,rank2=self.payroll))
  def __add__ (self,other):
    total_payroll = self.payroll + other.payroll

    return AmericanFootball(total_payroll)

class Defense:
  personel = "DL-LB-CB"
  position_type = 3

  def __init__(self,pass_rank="N/A",rush_rank="N/A",scheme=0):
    self.def_scheme = scheme
    self.def_pass_rank = pass_rank
    self.def_rush_rank = rush_rank

class Offense:
  personel = "QB-RB-WR-TE-OL"
  position_type = 5
  def __init__(self,pass_rank="N/A",rush_rank="N/A", scheme=0):
    self.off_scheme = scheme
    self.off_pass_rank = pass_rank
    self.off_rush_rank = rush_rank
  def __str__(self):
    return(" pass rank: {rank1} rush rank: {rank2}".format(rank1=self.off_pass_rank,rank2=self.off_rush_rank))
  def __add__ (self,other):
    total_pass_rank = self.off_pass_rank + other.off_pass_rank
    total_rush_rank = self.off_rush_rank + other.off_rush_rank
    return Offense(total_pass_rank,total_rush_rank)

henry = AmericanFootball("Vikings", 30)
victor = AmericanFootball("packers")
print(henry)
print (victor)
print(henry+victor)
print(henry.league_type)
henry = Offense(3,6)
victor  =Offense (4,8)
print(henry + victor)
print(henry.personel)
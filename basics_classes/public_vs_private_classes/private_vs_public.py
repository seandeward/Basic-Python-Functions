
#:: PUBLIC
# by default, all properties and methods in a class are public, meaning that you can access them with the "." operator
class Book:
  def __init__(self, name, author):
    self.name = name
    self.author = author

#:: PRIVATE
# Private data members are a way to encapsulate logic and data *within* a class definition. To make a property or method private, just prefix it with two underscores
class Wall:
  def __init__(self, phy_def, mag_def):
      self.__phy_def = phy_def
      self.__mag_def = mag_def
    # until __name and __author are called in a method, they are grayed out, since they are now private to the class

  def get_defenses(self):
    return self.__phy_def * self.__mag_def

front_wall = Wall(10, 2)
# results in an error
# print(front_wall.__armor)

# This works
print(front_wall.get_defenses()) # prints 20

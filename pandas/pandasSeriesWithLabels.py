import pandas as pd

a = [1,7,2]

# with the 'index' arguement, you can name your own labels
myvar = pd.Series(a, index = ["x", "y" "z"])

# prints all data
print(myvar)

# when you label items, you can access a specific item by referring to it's label
print(myvar["y"])
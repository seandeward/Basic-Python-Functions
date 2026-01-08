# list slicing
array = [1,2,3,4,5,6,7,8,9,10,11,12]

# SYNTAX: L[start:stop:step]

# this removes the first item from the array
array1 = array[1:]

# this keep ONLY the first one
array2 = array[:1]

# this removes everything except for the first 5 entries
array3 = array[0:5]

# this removes every other entry
array4 = array[::2]

# you can combine these three together for something really complicated if you want to
# this starts by removing the first, keeping every other third, until ending on 11
array5 = array[1:11:3]

print(array5)

#* Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.
    #* unlike lists, sets are unordered.



fruits = {"apple", "banana", "grape"}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}  





#* ADDING VALUES TO A SET
fruits = {"apple", "banana", "grape"}
fruits.add("pear")
print(fruits)
# Prints: {'pear', 'banana', 'grape', 'apple'}
    #? No error will be raised if you add an item already in the set, and the set will remain unchanged.

#* CREATING AN EMPTY SET
    # Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.
empty_set = set()

#* REMOVING A VALUE
fruits = {"apple", "banana", "grape"}
fruits.remove("grape")
print(fruits) # prints {'apple', 'banana'}

#* SET SUBTRACTION
set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
set3 = set1 - set2
    # or can just -- return set1 - set2

print(set3) # Prints: {'grape'}

#* CONVERTING A LIST INTO A SET
fruits = ["apple", "orange", "banana"] # example list
fruits_set = set(fruits) #? converting list to set
print(fruits_set)
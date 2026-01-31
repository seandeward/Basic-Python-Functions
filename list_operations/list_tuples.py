# tuples are collections of data that are ordered and unchangeable
# you can think of a tuple as a list with a fixed size.
# tuples are created with round brackets

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0]) # prints "this is a tuple"
print(my_tuple[1]) # prints 45
print(my_tuple[2]) # True

# while is generally bad practice to store items of different types in a List, it's not a problem with Tuples.
    # because they have a fixed size, it's easy to keep track of which indexes store which types of data
    # tuples are often used to store very small groups (like 2 or 3 items) of data.
        # For example, you might use a tuple to store a dog's name and age.
# === Example ===
dog = ("Fido", 4)

# There is a special case for creating single-item tuples. You must include a comma so Python knows it's a tuple and not regular parentheses
dog = ("Fido",)

# Because Tuples hold their data, multiple tuples can be stored within a list. Similar to storing other data in lists, each tuples, the first index selects which tuple you want to access, the second selects a value within that tuple.
my_tuples = [
    ("this is the first tuple in the list", 45, True),
    ("this is the second tuple in the list", 21, False)
]
print(my_tuples[0][0]) # this is the first tuple in the list
print(my_tuples[0][1]) # 45
print(my_tuples[1][0]) # this is the second tuple in the list
print(my_tuples[1][2]) # False
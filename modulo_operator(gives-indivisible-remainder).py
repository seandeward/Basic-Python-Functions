# * Modulo doesn't care about the result of the division, only the remainder of division

# for example, 7 % 2 = 1
    # this is because 2 goes into 7 three times, but gives a remainder of 1.
    # normally in 
    # the % operator returns the remainder



def is_even(x):
    return x % 2 == 0

print(is_even(5)) # prints False
print(is_even(4)) # prints True
def find_variation(array):
    from numpy import std # import standard deviation
    result = std(array)
    return result



# * testing area

speed_array = [86,87,88,86,87,85,86]

variation = find_variation(speed_array) * 100 # alternatively you can make it a percent and round it up, by multiplying by 100 and making it an integer respectively
print(f"{variation}%")
from numpy import percentile

def find_percentiles(array, percentage):
    result = percentile(array, percentage)
    return result

ages = [7,2,74,25,72,24,62,2,52,26,13,32]

percentile = int(find_percentiles(ages, 90)) # what is the age that 90% of people are younger than? # also make the number an integer

print(percentile)
import numpy # to get mean and median
from scipy import stats # to get mode

speed_array = [99,86,87,88,111,86,87,94,78,77,85,86]

mean = numpy.mean(speed_array) # take sum of array and divide by number of items

median = numpy.median(speed_array) # take the middlemost value in the array

mode = stats.mode(speed_array) # 

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode.mode}")
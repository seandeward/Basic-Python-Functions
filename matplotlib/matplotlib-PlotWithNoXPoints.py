# display several arrays of dnd character stats in arrays and create a couple of cool graphs with them

# import libraries
import numpy
#import pandas
import matplotlib.pyplot as pyplot
#import seaborn

# CHARACTER ARRAYS
# Char = int[Str, Dex, Con, Int, Wis, Cha]
Zook = numpy.array([21,20,18,11,9,6])
Samudra = numpy.array([13,18,16,12,14,16])
Mimir = numpy.array([13,12,16,14,18,16])
Eriol = numpy.array([8,12,16,15,18,16])

ypoints = numpy.array([3,8,1,10,5,7])

pyplot.plot(ypoints, marker = 'o', c = 'green')


# run the plot
pyplot.show()

# run program, and a window will show up
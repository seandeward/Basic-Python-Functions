# display several arrays of dnd character stats in arrays and create a couple of cool graphs with them

# import libraries
import numpy as np
#import pandas
import matplotlib.pyplot as plt
#import seaborn

# CHARACTER ARRAYS
# Char = int[Str, Dex, Con, Int, Wis, Cha]
#Zook = int[21,20,18,11,9,6]
#Samudra = int[13,18,16,12,14,16]
#Mimir = int[13,12,16,14,18,16]
#Eriol = int[8,12,16,15,18,16]

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
# run program, and a window will show up
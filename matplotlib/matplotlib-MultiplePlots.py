# display several arrays of dnd character stats in arrays and create a couple of cool graphs with them

# import libraries
import numpy as np
#import pandas
import matplotlib.pyplot as plt
#import seaborn

# CHARACTER ARRAYS
# Char = int[Str, Dex, Con, Int, Wis, Cha]
x = np.array(['Strength','Dexterity','Constitution','Wisdom','Charisma'])

# character stat number arrays
Zook = np.array([21,20,18,11,9,6])
Samudra = np.array([13,18,16,12,14,16])
Mimir = np.array([13,12,16,14,18,16])
Eriol = np.array([8,12,16,15,18,16])

plt.plot(Zook, c = 'red')
plt.plot(Samudra, c = 'blue')
plt.plot(Mimir, c = 'green')
plt.plot(Eriol, c = 'black')


# run the plot
plt.show()

# run program, and a window will show up
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
plt.scatter(Zook)
Samudra = np.array([13,18,16,12,14,16])
plt.scatter(Samudra)
Mimir = np.array([13,12,16,14,18,16])
plt.scatter(Mimir)
Eriol = np.array([8,12,14,15,18,16])
plt.scatter(Eriol)
Uno = np.array([8,14,14,20,16,13])
plt.scatter(Uno)
Ripley = np.array([14,20,17,13,14,14])
plt.scatter(Ripley)

titleFont = {'family':'serif','color':'#000a5b','size':20}
labelFont = {'family':'serif','color':'green','size':15}

# plot title and labels
plt.title("The Curse Breakers' Character Stats", fontdict = titleFont)
plt.xlabel('Character Stat', fontdict=labelFont)
plt.ylabel("Stat Amount", fontdict=labelFont)

# run the plot
plt.show()

# run program, and a window will show up
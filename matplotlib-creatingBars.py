# display several arrays of dnd character stats in arrays and create a couple of cool graphs with them

# import libraries
import numpy as np
#import pandas
import matplotlib.pyplot as plt
#import seaborn

# CHARACTER ARRAYS
# Char = int[Str, Dex, Con, Int, Wis, Cha]
x = np.array(["a","b","c","d","e","f"])

# character stat number arrays
Zook = np.array([21,20,18,11,9,6])
Samudra = np.array([13,18,16,12,14,16])
Mimir = np.array([13,12,16,14,18,16])
Eriol = np.array([8,12,14,15,18,16])
Uno = np.array([8,14,14,20,16,13])
Ripley = np.array([14,20,17,13,14,14])

plt.bar(x, Zook)
plt.bar(x, Samudra)
plt.bar(x, Mimir)
plt.bar(x, Eriol)
plt.bar(x, Uno)
plt.bar(x, Ripley)

titleFont = {'family':'serif','color':'#000a5b','size':20}
labelFont = {'family':'serif','color':'green','size':15}

# plot title and labels
plt.title("The Curse Breakers' Character Stats", fontdict = titleFont)
plt.xlabel('Character Stat', fontdict=labelFont)
plt.ylabel("Stat Amount", fontdict=labelFont)

# run the plot
plt.show()






import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
y2 = np.array([1,2,3,4])

plt.bar(x,y)
plt.bar(x,y2)
plt.show()
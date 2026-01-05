from matplotlib import pyplot as plt
from create_random_data_set import create_data_set

array = create_data_set(0, 5, 250)

plt.hist(array, 5)
plt.show()
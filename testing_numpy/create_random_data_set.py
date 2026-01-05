from numpy import random

def create_data_set(min=int(0), max=int(1), amount=(1)):
    result = random.uniform(min, max, amount)
    return result

random_array = create_data_set(0, 5, 250)

print(random_array)
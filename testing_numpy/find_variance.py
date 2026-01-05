from numpy import var
def find_variance(array):
    result = var(array)
    return result

speed = [1,2,3,4,5,6,3,6,8,5,2,5,6,7,3,4]

variance =  find_variance(speed)

print(variance)
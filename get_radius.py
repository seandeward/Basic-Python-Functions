# the value of the variable is passed to the function. It is assigned to a new variable called 'r'
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

radius = 5
area = area_of_circle(radius)
print(area)
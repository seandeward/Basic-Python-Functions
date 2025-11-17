# if statements inside variables to determine variable value
    # to test this, change the number of the variable "NumberOne" and see how the variable "Statement" changes to 5

NumberOne = 1 # variable "NumberOne" equals the numerical number 1
NumberFive = 5 # variable "NumberFive" equals the numerical number 5
Statement = NumberOne if NumberOne == 1 else NumberFive # varaible "Statement" will be "NumberOne" if variable "NumberOne" equals the number 1. If "NumberOne" equals anything else, "Statement" will become "NumberFive"
print(Statement) # print the "Statement" variable to the terminal
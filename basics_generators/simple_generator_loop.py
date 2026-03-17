# functions sometimes have a 'return' command that sends a value back to the main program. With Generators, you can have multiple "return" fields called 'yield' that report back to the main program.

def gen_values():
  yield 1
  print("yahoo1")
  yield 2
  print("yahoo2")
  yield 3
  

for value in gen_values(): # for each yield in the gen_values() function, continue through the program until each yield.
  print(value)


#? when are generators useful?
  # generators are great if you want to print results as they come, rather than having to print them out in one big result.
  # could techincally use them while debugging a function, but it's basically the same as just writing out print() statements.

#* FUNCTION VERSION
all_numbers = int(10)

def list_all_numbers(num_max:int):
  numbers = []
  for i in range(1, num_max + 1):
    numbers.append(i)
  return numbers

print(list_all_numbers(all_numbers)) # prints all numbers in a single list.


#* GENERATOR VERSION

def list_num_generator(nums:int):
  for i in range(1, nums + 1):
    yield i # prints one value


for value in list_num_generator(int(10)):
  print(value) # prints each number as a separate line.

for value in list_num_generator(int(20)):
  print(value)

#? you may notice that this generator is basically a for loop in of itself. While you could just make a for loop, generators are more modular and reuseable in a program, since they have arguements and parameters.
# they are also memory efficient!
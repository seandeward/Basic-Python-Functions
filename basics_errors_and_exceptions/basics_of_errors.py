
#* In Python, there are two main kinds of distinguishable errors:
    # Syntax errors
    # Exceptions

#* SYNTAX ERRORS
    # A syntax error is just the Python interpreter telling you that your code isn't adhering to proper Python syntax.

#* EXCEPTIONS
    # Exceptions are errors detected during execution, and are handles gracefully by your code.
    # You can even raise exceptions when bad things happen in your code
# * Python uses a try-except pattern for handling errors:
try:
    10 / 0
except Exception:
    print("can't divide by zero")

try:
    10 / 0
except Exception as e:
    print(e) # prints "division by zero"
    # * you can also -- return e
# Wrapping potential errors in try/except blocks allows the program to handle the exception gracefully without crashing.

#* Loss of network connectivity, missing database rows, out of memory issues, and unexpected user inputs can all prevent an application from performing "normally". It is your job to catch and handle any and all exceptions gracefully so that your app keeps working. 
#* When you are able to detect that something is amiss, you should be raising the errors yourself, in addition to the "default" exceptions that the Python interpreter will raise.
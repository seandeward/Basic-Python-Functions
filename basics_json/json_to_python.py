
import json

# some json
x = '{ "name":"John", "age":30, "city":"New York" }'

# parse the json
y = json.loads(x)

# the result is a python dictionary
print(y["age"])

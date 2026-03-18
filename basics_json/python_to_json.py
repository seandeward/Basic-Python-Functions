
import json

# a Python dictionary
x = {
  "name": "john",
  "age" : int(30),
  "city": "New York"
}

# convert to json
y = json.dumps(x)

# the result is a json string
print(y)
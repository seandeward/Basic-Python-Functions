
import json

with open("stuff.json") as test_json_file:
  stuff_file = json.load(test_json_file)

  print(type(stuff_file))

  print(stuff_file["name"])

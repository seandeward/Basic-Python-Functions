import json

# read the json after creating it
json_exists = None

try:
  open("output.json")
  json_exists = True
except:
  print("[!] output.json does not exist")
  # script ends

if json_exists:
  with open("output.json", mode="r", encoding="utf-8") as dummy_json:
    print(json.load(dummy_json))

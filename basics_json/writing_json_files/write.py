
import json

# python dictionary as input
dummy_data = {
  "dogs"   :   30,
  "cats"   :   25,
  "hamsters" : 12
}

# write the json file
with open("output.json", mode="w", encoding="utf-8") as dummy_json_file:
  json.dump(dummy_data, dummy_json_file, sort_keys=True, indent=2) # "sort_keys=True, indent=2" added for styling, not required for function

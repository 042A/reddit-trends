import json

my_dict = {
    "name": "Trulsa",
    "species": "Doggo",
    "age": 8,
    "angry": False,
    "other_names": ["doggen", "good boy", "byracka"]
 }


f = open("file.json", "w")
json.dump(my_dict, f, indent=3) 

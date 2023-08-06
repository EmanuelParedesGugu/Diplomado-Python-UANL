import json

dict1 = {
"emp1": {
"name": "Lisa",
"designation":"programmer",
"age": "34"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(dict1, write_file)
import json
personal_info = {
    "name": "Ahmed",
    "age": 21,
    "gender": "male"
}

with open('info.json', "w") as json_file:
    json.dump(personal_info, json_file)

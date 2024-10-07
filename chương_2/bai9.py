import json
dic = {
    "city": "Hanoi",
    "name": "Nguyen Van Nam",
    "age": 19,
    "mon_hoc": ["toan", "vatli", "hoa"]
}
json_data = json.dumps(dic, sort_keys=True, indent=4)
print(json_data)

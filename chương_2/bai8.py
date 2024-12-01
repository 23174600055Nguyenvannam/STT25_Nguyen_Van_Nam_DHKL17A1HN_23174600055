import json
chuoi_obj = {"name": "Nguyen Van Nam", "age": 21, "city": "Hanoi"}
du_lieu_data = json.dumps(chuoi_obj)
print("Chuỗi JSON:", du_lieu_data)
for value in chuoi_obj.values():
    print(value)

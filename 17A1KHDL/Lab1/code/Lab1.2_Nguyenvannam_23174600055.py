import json
class JSONReader:
    def __init__(self,file_path):
        self.file_path =file_path
        self.data = None

    def read_Json(self):
        with open(self.file_path, 'r')as file:
            self.data = json.load(file)
    
    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name : {user['name']}, Age : {user['age']}, address: {user['address']}")

path = r'Lab1\data\users.json'
reader = JSONReader(path)
reader.read_Json()
reader.display_data()
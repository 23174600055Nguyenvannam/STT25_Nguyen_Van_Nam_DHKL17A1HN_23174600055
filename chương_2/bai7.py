import json

# Sử dụng đường dẫn đầy đủ đến file JSON
with open('D:/New folder (2)/Nguyen_Van_Nam_DHKL17A1HN_23174600055/chương_2/data.json') as json_file:
    data = json.load(json_file)

# In dữ liệu
print(data)

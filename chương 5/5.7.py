import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Cập nhật tất cả các giá trị trong cột 'age' (tăng thêm 5 tuổi)
cursor.execute("UPDATE users SET age = age + 5;")
conn.commit()

# Hiển thị dữ liệu sau khi cập nhật
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()
print("Dữ liệu sau khi cập nhật:", rows)

conn.close()


import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Tạo bảng và chèn dữ liệu
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER);")
cursor.executemany("INSERT INTO users (id, name, age) VALUES (?, ?, ?);", [(1, "Alice", 25), (2, "Bob", 30)])
conn.commit()

# Hiển thị dữ liệu
cursor.execute("SELECT * FROM users;")
print(cursor.fetchall())

conn.close()

import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Liệt kê các bảng
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Các bảng trong cơ sở dữ liệu:", tables)

conn.close()
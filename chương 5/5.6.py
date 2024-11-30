import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Đếm số bản ghi
cursor.execute("SELECT COUNT(*) FROM users;")
count = cursor.fetchone()[0]
print(f"Số bản ghi trong bảng 'users': {count}")

conn.close()
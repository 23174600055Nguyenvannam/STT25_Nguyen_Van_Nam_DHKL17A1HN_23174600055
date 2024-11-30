import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Xóa một hàng cụ thể (dựa trên id)
cursor.execute("DELETE FROM users WHERE id = 1;")
conn.commit()

# Hiển thị dữ liệu sau khi xóa
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()
print("Dữ liệu sau khi xóa:", rows)

conn.close()
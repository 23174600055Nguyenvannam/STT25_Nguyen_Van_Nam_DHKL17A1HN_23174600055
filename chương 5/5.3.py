import sqlite3

# Tạo hoặc kết nối tới cơ sở dữ liệu
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Tạo bảng trong cơ sở dữ liệu
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
""")
print("Bảng 'users' đã được tạo.")
conn.commit()
conn.close()
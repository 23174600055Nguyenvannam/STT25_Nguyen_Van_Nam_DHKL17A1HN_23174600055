import sqlite3

conn = sqlite3.connect("ql_nhan_vien.db")
cursor = conn.cursor()

# Tạo bảng phòng ban và nhân viên
cursor.execute("CREATE TABLE IF NOT EXISTS PHONG (id INTEGER PRIMARY KEY, name TEXT, price REAL, amount INTEGER);")
cursor.execute("CREATE TABLE IF NOT EXISTS NHANVIEN (id INTEGER PRIMARY KEY, name TEXT, phong_id INTEGER, FOREIGN KEY(phong_id) REFERENCES PHONG(id));")
conn.commit()

# Thêm phòng ban và nhân viên
cursor.execute("INSERT INTO PHONG (name, price, amount) VALUES ('Phòng IT', 1000, 10);")
cursor.execute("INSERT INTO NHANVIEN (name, phong_id) VALUES ('Nguyễn A', 1);")
conn.commit()

# Hiển thị nhân viên theo phòng ban
cursor.execute("SELECT * FROM NHANVIEN WHERE phong_id = 1;")
print(cursor.fetchall())

conn.close()
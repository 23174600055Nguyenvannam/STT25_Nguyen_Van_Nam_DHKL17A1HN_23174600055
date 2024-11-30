import sqlite3

# Kết nối tới cơ sở dữ liệu trong bộ nhớ
conn = sqlite3.connect(":memory:")
print("Đã kết nối tới cơ sở dữ liệu trong bộ nhớ.")
conn.close()

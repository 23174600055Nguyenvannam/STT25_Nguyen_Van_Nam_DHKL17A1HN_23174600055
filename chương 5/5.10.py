import sqlite3

conn = sqlite3.connect("product.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, name TEXT, price REAL, amount INTEGER);")
conn.commit()

# Thêm sản phẩm
cursor.execute("INSERT INTO product (name, price, amount) VALUES ('Product A', 10.5, 100);")
conn.commit()

# Hiển thị sản phẩm
cursor.execute("SELECT * FROM product;")
print(cursor.fetchall())

conn.close()

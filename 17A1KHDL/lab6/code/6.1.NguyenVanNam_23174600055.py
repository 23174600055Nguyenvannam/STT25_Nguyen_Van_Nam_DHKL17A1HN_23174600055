import sqlite3

def ket_noi_csdl():
    return sqlite3.connect("product.db")

def tao_bang():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute('''
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    ''')
    ket_noi.commit()
    ket_noi.close()

if __name__ == "__main__":
    tao_bang()
    print("Bảng product đã được tạo thành công.")

import sqlite3

def tao_co_so_du_lieu():
    ket_noi = sqlite3.connect("product.db")
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
    print("Cơ sở dữ liệu và bảng 'product' đã được tạo thành công.")

if __name__ == "__main__":
    tao_co_so_du_lieu()

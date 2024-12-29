import sqlite3

def ket_noi_csdl():
    return sqlite3.connect(r"D:\17A1KHDL\lab4\data\product.db")

def hien_thi_san_pham():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT * FROM product")
    danh_sach = con_tro.fetchall()
    ket_noi.close()

    if danh_sach:
        print(f"{'ID':<5}{'Tên':<20}{'Giá':<10}{'Số Lượng':<10}")
        for sp in danh_sach:
            print(f"{sp[0]:<5}{sp[1]:<20}{sp[2]:<10}{sp[3]:<10}")
    else:
        print("Không có sản phẩm nào trong cơ sở dữ liệu.")

def them_san_pham():
    ket_noi = ket_noi_csdl()
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))
    so_luong = int(input("Nhập số lượng sản phẩm: "))
    con_tro = ket_noi.cursor()
    con_tro.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (ten, gia, so_luong))
    ket_noi.commit()
    ket_noi.close()
    print("Thêm sản phẩm thành công.")

# Tìm kiếm sản phẩm theo tên
def tim_kiem_san_pham():
    ket_noi = ket_noi_csdl()
    ten = input("Nhập tên sản phẩm cần tìm: ")
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + ten + '%',))
    danh_sach = con_tro.fetchall()
    ket_noi.close()

    if danh_sach:
        print(f"{'ID':<5}{'Tên':<20}{'Giá':<10}{'Số Lượng':<10}")
        for sp in danh_sach:
            print(f"{sp[0]:<5}{sp[1]:<20}{sp[2]:<10}{sp[3]:<10}")
    else:
        print("Không tìm thấy sản phẩm nào.")

# Cập nhật thông tin sản phẩm
def cap_nhat_san_pham():
    ket_noi = ket_noi_csdl()
    ma_sp = int(input("Nhập ID sản phẩm cần cập nhật: "))
    gia_moi = float(input("Nhập giá mới: "))
    so_luong_moi = int(input("Nhập số lượng mới: "))
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (gia_moi, so_luong_moi, ma_sp))
    ket_noi.commit()
    ket_noi.close()
    print("Cập nhật sản phẩm thành công.")

# Xóa sản phẩm
def xoa_san_pham():
    ket_noi = ket_noi_csdl()
    ma_sp = int(input("Nhập ID sản phẩm cần xóa: "))
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM product WHERE Id = ?", (ma_sp,))
    ket_noi.commit()
    ket_noi.close()
    print("Xóa sản phẩm thành công.")

# Menu điều khiển
def main():
    while True:
        print("\n--- MENU QUẢN LÝ SẢN PHẨM ---")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")
        lua_chon = input("Chọn chức năng (1-6): ")
        
        if lua_chon == "1":
            hien_thi_san_pham()
        elif lua_chon == "2":
            them_san_pham()
        elif lua_chon == "3":
            tim_kiem_san_pham()
        elif lua_chon == "4":
            cap_nhat_san_pham()
        elif lua_chon == "5":
            xoa_san_pham()
        elif lua_chon == "6":
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()

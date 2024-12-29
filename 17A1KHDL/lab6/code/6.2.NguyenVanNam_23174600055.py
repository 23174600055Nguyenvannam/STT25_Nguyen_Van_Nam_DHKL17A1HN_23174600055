import tkinter as tk
import sqlite3

# Kết nối đến cơ sở dữ liệu
def ket_noi_csdl():
    """Kết nối đến cơ sở dữ liệu SQLite."""
    return sqlite3.connect(r"D:\17A1KHDL\lab6\data\product.db")

# Tạo bảng product nếu chưa tồn tại
def tao_bang():
    """Tạo bảng product nếu chưa tồn tại."""
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

# Hàm hiển thị thông báo
def hien_thi_thong_bao(loai, noi_dung):
    """Hiển thị thông báo thành công hoặc lỗi."""
    label_thong_bao.config(text=noi_dung, fg="green" if loai == "thanh_cong" else "red")

# Hàm thêm sản phẩm
def them_san_pham():
    ten = entry_name.get()
    gia = entry_price.get()
    so_luong = entry_amount.get()

    if not ten or not gia or not so_luong:
        hien_thi_thong_bao("loi", "Vui lòng điền đầy đủ thông tin.")
        return

    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (ten, float(gia), int(so_luong)))
    ket_noi.commit()
    ket_noi.close()
    hien_thi_thong_bao("thanh_cong", "Thêm sản phẩm thành công!")
    lam_moi_danh_sach()

# Hàm xóa sản phẩm
def xoa_san_pham():
    selected_item = listbox_products.get(listbox_products.curselection())
    prod_id = selected_item.split(" - ")[0]
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM product WHERE Id = ?", (prod_id,))
    ket_noi.commit()
    ket_noi.close()
    hien_thi_thong_bao("thanh_cong", "Xóa sản phẩm thành công!")
    lam_moi_danh_sach()

# Hàm tìm kiếm sản phẩm
def tim_kiem_san_pham():
    keyword = entry_search.get()
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + keyword + '%',))
    results = con_tro.fetchall()
    ket_noi.close()

    listbox_products.delete(0, tk.END)
    for prod in results:
        listbox_products.insert(tk.END, f"{prod[0]} - {prod[1]} - Giá: {prod[2]} - SL: {prod[3]}")

# Hàm làm mới danh sách
def lam_moi_danh_sach():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT * FROM product")
    products = con_tro.fetchall()
    ket_noi.close()

    listbox_products.delete(0, tk.END)
    for prod in products:
        listbox_products.insert(tk.END, f"{prod[0]} - {prod[1]} - Giá: {prod[2]} - SL: {prod[3]}")

# Hàm cập nhật sản phẩm
def cap_nhat_san_pham():
    selected_item = listbox_products.get(listbox_products.curselection())
    prod_id = selected_item.split(" - ")[0]
    ten = entry_name.get()
    gia = entry_price.get()
    so_luong = entry_amount.get()

    if not ten or not gia or not so_luong:
        hien_thi_thong_bao("loi", "Vui lòng điền đầy đủ thông tin.")
        return

    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE product SET Name = ?, Price = ?, Amount = ? WHERE Id = ?", (ten, float(gia), int(so_luong), prod_id))
    ket_noi.commit()
    ket_noi.close()
    hien_thi_thong_bao("thanh_cong", "Cập nhật sản phẩm thành công!")
    lam_moi_danh_sach()

# Giao diện chính
root = tk.Tk()
root.title("Quản Lý Sản Phẩm")

# Tạo bảng nếu chưa tồn tại
tao_bang()

# Tạo các widget giao diện
tk.Label(root, text="Tên sản phẩm:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Giá sản phẩm:").grid(row=1, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Số lượng:").grid(row=2, column=0, padx=10, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Thêm sản phẩm", command=them_san_pham).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Cập nhật sản phẩm", command=cap_nhat_san_pham).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Xóa sản phẩm", command=xoa_san_pham).grid(row=4, column=0, padx=10, pady=5)

tk.Label(root, text="Tìm kiếm:").grid(row=5, column=0, padx=10, pady=5)
entry_search = tk.Entry(root)
entry_search.grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Tìm kiếm", command=tim_kiem_san_pham).grid(row=5, column=2, padx=10, pady=5)

listbox_products = tk.Listbox(root, width=50)
listbox_products.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Label thông báo
label_thong_bao = tk.Label(root, text="", fg="red")
label_thong_bao.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

# Làm mới danh sách khi khởi động
lam_moi_danh_sach()

# Chạy ứng dụng
root.mainloop()

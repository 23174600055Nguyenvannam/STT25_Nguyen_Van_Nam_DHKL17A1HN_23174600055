class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        """Khởi tạo phân số với tử số và mẫu số."""
        self.tu_so = tu_so
        self.mau_so = mau_so

    def nhap_phan_so(self):
        """Nhập tử số và mẫu số từ người dùng."""
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))

    def rut_gon(self):
        """Rút gọn phân số."""
        ucln = self.uoc_chung_lon_nhat(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def uoc_chung_lon_nhat(self, a, b):
        """Tìm ước chung lớn nhất (UCLN) của a và b."""
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def in_phan_so(self):
        """In phân số ra màn hình."""
        print(f"{self.tu_so}/{self.mau_so}")

# Sử dụng chương trình
ps = PhanSo()
ps.nhap_phan_so()
ps.rut_gon()
ps.in_phan_so()

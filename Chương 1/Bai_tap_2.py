class Thisinh:
    def __init__(self,ho_van_ten = "", diem_mon_toan = 0,diem_mon_ly = 0 , diem_mon_hoa = 0):
        self.ho_va_ten = ho_van_ten
        self.diem_mon_toan = diem_mon_toan
        self.diem_mon_ly = diem_mon_ly
        self.diem_mon_hoa = diem_mon_hoa

        
    def nhap_thong_tin(self):
        self.ho_va_ten = input("Nhập họ và tên học sinh:")
        self.diem_mon_toan = float(input("Nhập điểm môn toán:"))
        self.diem_mon_ly = float(input("Nhập điểm môn lý:"))
        self.diem_mon_hoa = float(input("Nhập điểm môn hoá:"))


    def tinh_tong_diem (self):
        self.tong_diem = self.diem_mon_toan + self.diem_mon_ly + self.diem_mon_hoa
        return self.tong_diem
        
    def in_thong_tin(self):
        print("Họ và tên : {}".format(self.ho_va_ten))
        print("Điểm môn toán : {}".format(self.diem_mon_toan))
        print("Điểm môn lý : {}".format(self.diem_mon_ly))
        print("Điểm môn hoá: {}".format(self.diem_mon_hoa))
        print("Tổng điểm : {}".format(self.tinh_tong_diem()))
Ts = Thisinh()
Ts.nhap_thong_tin()
Ts.in_thong_tin()
    

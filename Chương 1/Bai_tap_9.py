# Lớp đa giác cơ bản
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

class HinhBinhHanh(DaGiac):
    def __init__(self, day, chieu_cao, canh_ben):
        super().__init__(4)  
        self.day = day
        self.chieu_cao = chieu_cao
        self.canh_ben = canh_ben

    def chu_vi(self):
        return 2 * (self.day + self.canh_ben)

    def dien_tich(self):
        return self.day * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_rong)  
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)  
    def chu_vi(self):
        return 4 * self.chieu_dai

    def dien_tich(self):
        return self.chieu_dai * self.chieu_dai

hinh_binh_hanh = HinhBinhHanh(10, 5, 7)
print("Hình bình hành: Chu vi =", hinh_binh_hanh.chu_vi(), ", Diện tích =", hinh_binh_hanh.dien_tich())

hinh_chu_nhat = HinhChuNhat(10, 5)
print("Hình chữ nhật: Chu vi =", hinh_chu_nhat.chu_vi(), ", Diện tích =", hinh_chu_nhat.dien_tich())

hinh_vuong = HinhVuong(5)
print("Hình vuông: Chu vi =", hinh_vuong.chu_vi(), ", Diện tích =", hinh_vuong.dien_tich())

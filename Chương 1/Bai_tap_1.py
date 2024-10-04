class HCN:
    def __init__(self,chieu_dai,chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self):
        self.tinh_chu_vi = (self.chieu_dai +self.chieu_rong)*2
        return self.tinh_chu_vi
    
    def dien_tich(self):
        self.tinh_dien_tich = self.chieu_dai * self.chieu_rong
        return self.tinh_dien_tich

a = int(input("Nhập chiều dài:"))
b = int(input("Nhập chiều rộng:"))

hcn = HCN(a,b)
chu_vi = hcn.chu_vi()
dien_tich = hcn.dien_tich()

print("chiều dài là : {}".format(a))
print("chiều rộng là : {}".format(b))
print("chu vi hình chữ nhật là :",chu_vi)
print("diện tích hình chữ nhật là:", dien_tich)
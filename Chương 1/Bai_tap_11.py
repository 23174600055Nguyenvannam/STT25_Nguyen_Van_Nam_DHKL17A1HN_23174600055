import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def chu_vi(self):
        return self.a + self.b + self.c
    
class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a**2 + b**2))  

    def dien_tich(self):
        return (self.a * self.b) / 2
    
class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_khac):
        super().__init__(canh_bang, canh_bang, canh_khac)

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)

    def dien_tich(self):
        return (math.sqrt(3) / 4) * self.a ** 2


tam_giac_vuong = TamGiacVuong(3, 4)  
print("Tam giác vuông: Chu vi =", tam_giac_vuong.chu_vi(), ", Diện tích =", tam_giac_vuong.dien_tich())

tam_giac_can = TamGiacCan(5, 6)  
print("Tam giác cân: Chu vi =", tam_giac_can.chu_vi())

tam_giac_deu = TamGiacDeu(6) 
print("Tam giác đều: Chu vi =", tam_giac_deu.chu_vi(), ", Diện tích =", tam_giac_deu.dien_tich())

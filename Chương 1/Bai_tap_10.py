import math
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y) 
        self.ban_truc_lon = ban_truc_lon
        self.ban_truc_nho = ban_truc_nho

    def dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)  

elip = Elip(0, 0, 4, 2) 
print("Diện tích elip =", elip.dien_tich())

duong_tron = DuongTron(0, 0, 3)  
print("Diện tích đường tròn =", duong_tron.dien_tich())  

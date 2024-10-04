class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày {self.day}/{self.month}/{self.year}")

    def next(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day += 1  
        if self.day > days_in_month[self.month - 1]:
            self.day = 1  
            self.month += 1 
        if self.month > 12:
            self.month = 1 
            self.year += 1 

d = Date(30, 4, 2023) 
d.display() 

d.next() 
d.display()  

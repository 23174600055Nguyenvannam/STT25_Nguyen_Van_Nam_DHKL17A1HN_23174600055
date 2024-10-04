class Date:
    def __init__(self, day=20, month=5, year=2005):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

class Employee:
    def __init__(self, name, dob, hire_date):
        self.name = name
        self.dob = dob 
        self.hire_date = hire_date  

    def display(self):
        print(f"Họ tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.dob.display() 
        print("Ngày vào công ty: ", end="")
        self.hire_date.display()  
dob = Date(20, 5, 1005)  
hire_date = Date(1, 7, 2024)  

employee = Employee("Nguyễn Văn A", dob, hire_date) 
employee.display() 

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.stack = []          
        self.top = -1             

    def __del__(self):
        del self.stack

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.stack.append(value) 
            self.top += 1
            print(f"Đã thêm phần tử {value} vào ngăn xếp.")

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể lấy phần tử.")
            return None
        else:
            popped_value = self.stack.pop()  
            self.top -= 1
            print(f"Đã lấy phần tử {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        """Kiểm tra ngăn xếp có đầy không."""
        return self.top == self.capacity - 1

    def count(self):
        """Trả về số lượng phần tử hiện tại trong ngăn xếp."""
        return self.top + 1

    def display(self):
        """Hiển thị các phần tử trong ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Các phần tử trong ngăn xếp:", self.stack)



stack = Stack(5)  

stack.push(10.5) 
stack.push(20.1)  
stack.push(30.2)  

print(f"Số phần tử hiện tại trong ngăn xếp: {stack.count()}") 

stack.pop()  

print(f"Số phần tử hiện tại trong ngăn xếp: {stack.count()}")  

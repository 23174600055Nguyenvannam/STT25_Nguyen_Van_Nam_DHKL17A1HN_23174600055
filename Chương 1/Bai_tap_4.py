class Stack:
    def __init__(self, capacity):
        """Hàm tạo để khởi tạo ngăn xếp với kích thước cố định."""
        self.capacity = capacity  # Sức chứa tối đa của ngăn xếp
        self.stack = []           # Mảng động (danh sách) lưu các phần tử ngăn xếp
        self.top = -1             # Chỉ số của phần tử đỉnh ngăn xếp

    def __del__(self):
        """Hàm hủy tự động được gọi khi đối tượng không còn được sử dụng."""
        del self.stack

    def push(self, value):
        """Đưa một phần tử vào ngăn xếp."""
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.stack.append(value)  # Thêm phần tử vào danh sách
            self.top += 1
            print(f"Đã thêm phần tử {value} vào ngăn xếp.")

    def pop(self):
        """Lấy một phần tử ra khỏi ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể lấy phần tử.")
            return None
        else:
            popped_value = self.stack.pop()  # Lấy phần tử từ danh sách
            self.top -= 1
            print(f"Đã lấy phần tử {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    def isEmpty(self):
        """Kiểm tra ngăn xếp có rỗng không."""
        return self.top == -1

    def isFull(self):
        """Kiểm tra ngăn xếp có đầy không."""
        return self.top == self.capacity - 1

    def display(self):
        """Hiển thị các phần tử trong ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Các phần tử trong ngăn xếp:", self.stack)


# Ví dụ sử dụng lớp Stack
stack = Stack(5)  # Tạo ngăn xếp với sức chứa tối đa là 5 phần tử

stack.push(10.5)  # Thêm phần tử 10.5 vào ngăn xếp
stack.push(20.1)  # Thêm phần tử 20.1 vào ngăn xếp
stack.push(30.2)  # Thêm phần tử 30.2 vào ngăn xếp

stack.display()  # Hiển thị các phần tử trong ngăn xếp

stack.pop()  # Lấy phần tử ra khỏi ngăn xếp

stack.display()  # Hiển thị lại ngăn xếp sau khi pop

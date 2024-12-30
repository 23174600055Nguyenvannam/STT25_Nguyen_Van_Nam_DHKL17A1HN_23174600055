import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Chương trình xem ảnh")

# Mở và chỉnh kích thước ảnh
image = Image.open(r"Nguyen_Van_Nam_DHKL17A1HN_23174600055\chương 7\oto.jpg")
new_size = (400, 400)
image = image.resize(new_size, Image.Resampling.LANCZOS)

# Chuyển ảnh sang định dạng hiển thị trong Tkinter
img = ImageTk.PhotoImage(image)

# Tạo nhãn và gắn ảnh
label = tk.Label(window, image=img)
label.image = img 
label.pack()

window.mainloop()
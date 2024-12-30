import tkinter as tk
window = tk.Tk()
window.title("tk")
window.geometry("380x80")

label = tk.Label(window,text="Enter a word")
label.grid(row=0,column=0)
text_label = tk.Entry(window,width=15)
text_label.grid(row=0,column=1)

label2 = tk.Label(window,text="")
label2.grid(row=1,column=1)
def dao_nguoc(arr):
    chuoi_nguoc=''
    for i in arr:
        chuoi_nguoc = i+chuoi_nguoc
    return chuoi_nguoc
def validate():
    user_input = text_label.get()
    reverse = dao_nguoc(user_input)
    label2.configure(text=reverse)

button = tk.Button(window,text="Validate",command=validate)
button.grid(row=2,column=1)
window.mainloop()
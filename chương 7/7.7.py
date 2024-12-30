import tkinter as tk
window = tk.Tk()
window.title('tk')
window.geometry('480x80')

label= tk.Label(window,text="Enter value of integer N: ")
label.grid(row=0,column=0)

text_label = tk.Entry(window,width=15)
text_label.grid(row=0,column=1)

label1 = tk.Label(window,text="")
label1.grid(row=1,column=1)


def sum_n(n):
    s=0
    for i in range(n+1):
        s+=i
    return s
def tinh_tong():
    user_input = int(text_label.get())
    summ = sum_n(user_input)
    text = f"The sum is 1+2+3+...+{user_input} = {summ}"
    label1.configure(text=text)
button = tk.Button(window,text = 'Validate',command=tinh_tong)
button.grid(row=2,column=1)
window.mainloop()
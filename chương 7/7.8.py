import tkinter as tk
def uoc_so(n):
    danh_sach=[]
    for i in range(1,n):
        if n%i==0:
            danh_sach.append(i)
    return danh_sach

window = tk.Tk()
window.title("uoc so")
window.geometry("380x80")

lbl1 = tk.Label(window,text="Enter the value of N")
lbl1.grid(row=0,column=0)

lbl2= tk.Label(window,text= "The divisor of N:")
lbl2.grid(row=1,column=0)

text_label = tk.Entry(window,width=15)
text_label.grid(row=0,column=1)

lbl3 = tk.Label(window,text="")
lbl3.grid(row=1,column=1)

def cac_uoc():
    user_text = int(text_label.get())
    uocso = uoc_so(user_text)
    lbl3.configure(text=uocso)
button = tk.Button(window,text = "Validate",command=cac_uoc)
button.grid(row=2,column=1)
window.mainloop()
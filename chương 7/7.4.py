import tkinter as tk

class SinhVien:
    def __init__(self,root):
        self.root = root
        self.root.title('Welcome app sinh vien')
        self.root.geometry("380x80")
        
        self.lbl1 = tk.Label(self.root,text= 'id')
        self.lbl1.grid(row=0,column=0)

        self.lbl2 = tk.Label(self.root,text = "ten sinh vien")
        self.lbl2.grid(row=1,column=0)

        self.lbl3 = tk.Label(self.root,text = "mat khau")
        self.lbl3.grid(row=2,column=0)

        self.text1 = tk.Entry(self.root,width=15)
        self.text1.grid(row=0,column=1)
        self.text1.focus()

        self.text2 = tk.Entry(self.root,width=15)
        self.text2.grid(row=1,column=1)
        self.text2.focus()

        self.text3 = tk.Entry(self.root,width=15)
        self.text3.grid(row=2,column=1)
        self.text3.focus()
root = tk.Tk()
app = SinhVien(root)
root.mainloop()
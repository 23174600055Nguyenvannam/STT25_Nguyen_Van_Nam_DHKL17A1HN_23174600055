import tkinter as tk
window = tk.Tk()
window.geometry("400x100")
window.title("hello world")

label = tk.Label(window,text = "hello", font= ('Arial',50,'italic'))
label.grid(row=0,column=0)

def chang_font():
    label.configure(font= ('Helvetica',20,'bold'))

button = tk.Button(window,text='change font',command=chang_font)
button.grid(row=0,column=1)
window.mainloop()
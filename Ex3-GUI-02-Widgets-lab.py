import tkinter as tk
groot = tk.Tk()
groot.geometry("300x300")

def changeback():
    user = listbox.curselection()
    text2 = listbox.get(user)
    LB.configure(text=text2)
    groot.configure(bg=listbox.get(user))


listbox = tk.Listbox(groot,selectmode=tk.SINGLE,height=7)
listbox.insert(1,"blue")
listbox.insert(2,"red")
listbox.insert(3,"purple")
listbox.insert(4,"black")
listbox.insert(5,"green")
listbox.insert(6,"orange")
listbox.pack()
listbox.select_set(0)

but = tk.Button(groot,text="PRESS",command=changeback)
but.pack()

LB = tk.Label(groot,text="")
LB.pack()


groot.mainloop()
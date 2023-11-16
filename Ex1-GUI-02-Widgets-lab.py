import tkinter as tk
root = tk.Tk()
root.geometry("300x300")

lab = tk.Label(root,text="HELLO")
lab.pack()

ent1 = tk.Entry(root)
ent1.pack()

def copytext():
    lab.configure(text=ent1.get())
    root.configure(bg= ent1.get())
    

butt = tk.Button(root,text="Button",height=1,width=9,command= copytext)
butt.pack()


root.mainloop()
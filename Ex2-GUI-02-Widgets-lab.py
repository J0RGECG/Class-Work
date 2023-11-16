import tkinter as tk
groot = tk.Tk()
groot.geometry("300x300")
radio = tk.Variable()
radio.set(2)
myboo = tk.Variable
myboo2= tk.Variable
myboo3= tk.Variable
myboo4= tk.Variable



def dothisdown():
    myvar = radio.get()
    label2.configure(text=myvar)
    if myboo == 1:
        label3.configure(text=myboo.get())

        

myradio = tk.Radiobutton(groot)
myradio.configure(text="cat",variable=radio,value="cat")

myradio2 = tk.Radiobutton(groot)
myradio2.configure(text="dog",variable=radio,value="dog")

myradio3 = tk.Radiobutton(groot)
myradio3.configure(text="fish",variable=radio,value="fish")

myradio4 = tk.Radiobutton(groot)
myradio4.configure(text="cow",variable=radio,value="cow")

label2 = tk.Label(groot,text=" ")

label1 = tk.Label(groot,text="---------------------")

checkbox1 = tk.Checkbutton(groot,text="Checkbutton 1")
checkbox1.configure(variable=myboo)
checkbox2 = tk.Checkbutton(groot,text="Checkbutton 2",variable=myboo2)
checkbox3 = tk.Checkbutton(groot,text="Checkbutton 3",variable=myboo3)
checkbox4 = tk.Checkbutton(groot,text="Checkbutton 4",variable=myboo4)


label3 = tk.Label(groot,text="q")

button = tk.Button(groot,text="PRESS ME",command=dothisdown)

myradio.pack()
myradio2.pack()
myradio3.pack()
myradio4.pack()
label2.pack()
label1.pack()
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()
checkbox4.pack()
label3.pack()

button.pack()

groot.mainloop()
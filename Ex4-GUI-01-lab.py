import tkinter as tk
import random



groot = tk.Tk()
groot.geometry("300x300")
Ran = random.randint(0,101)


def dothis():
    LB.configure(text="You have pushed the button")



def dothis123():
    LB.configure(text= "Your Ramdom Number")
    LB2.configure(text= Ran)
    BUT2.configure(bg="blue")

    


LB = tk.Label(groot,text = "Hello there User" )
LB.pack()


LB2 = tk.Label(groot,text = " Second Label",font=( 'arial',25 ))
LB2.configure(bg="red")
LB2.configure(fg="black")
LB2.pack()

    
BUT = tk.Button(groot,text= "Button One", command= dothis)
BUT.pack()


BUT2 = tk.Button(groot,text= "Button Two" ,height=3,width=9 ,command= dothis123)
BUT2.pack()


groot.mainloop()
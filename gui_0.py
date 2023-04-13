from tkinter import *

root = Tk()
# creating label widget 
#myLabel1 = Label(root, text="hello world").grid(row=0, column=0)
#myLabel2 = Label(root, text="maj nejm is majsner").grid(row=1, column=1)

e = Entry(root, width=50, bg="yellow", border=5 )
e.pack()
e.insert(0,"Enter your name here")

def myClick():
    myLabel = Label(root, text= "Hello " + e.get())
    myLabel.pack()
 
myButton = Button(root,text="Enter your name", command=myClick, bg="blue",fg="white")
myButton.pack()

root.mainloop()

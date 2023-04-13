from tkinter import *

root = Tk()
root.title("Moje účty")

# creating label widget 
#myLabel1 = Label(root, text="hello world").grid(row=0, column=0)
#myLabel2 = Label(root, text="maj nejm is majsner").grid(row=1, column=1)

e = Entry(root, width=50, bg="yellow", border=5 )
e.grid(row = 0,column = 0, columnspan = 3,padx = 10,pady = 10)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num +int(second_number))


#define buttons
button1= Button(root,text="1",command=lambda: button_click(1), padx = 40, pady = 20)
button2= Button(root,text="2",command=lambda: button_click(2), padx = 40, pady = 20)
button3= Button(root,text="3",command=lambda: button_click(3), padx = 40, pady = 20)
button4= Button(root,text="4",command=lambda: button_click(4), padx = 40, pady = 20)
button5= Button(root,text="5",command=lambda: button_click(5), padx = 40, pady = 20)
button6= Button(root,text="6",command=lambda: button_click(6), padx = 40, pady = 20)
button7= Button(root,text="7",command=lambda: button_click(7), padx = 40, pady = 20)
button8= Button(root,text="8",command=lambda: button_click(8), padx = 40, pady = 20)
button9= Button(root,text="9",command=lambda: button_click(9), padx = 40, pady = 20)
button0= Button(root,text="0",command=lambda: button_click(0), padx = 40, pady = 20)
button_add= Button(root,text="+",command=button_add, padx = 40, pady = 20)
button_equal= Button(root,text="=",command=button_equal, padx = 94, pady = 20)
button_clear= Button(root,text="Clear",command=button_clear, padx = 86, pady = 20)
#put the button on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_equal.grid(row=4,column=1,columnspan = 2)
button_add.grid(row=5,column = 0)
button_clear.grid(row=5, column=1,columnspan = 2)


root.mainloop()
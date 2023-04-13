from tkinter import *
from tkinter import ttk
import time
from tqdm import tqdm
from tkinter.messagebox import showinfo
#dodelat tlacitko odhlasit se v account frame pomoci (tkraise)
    #login_frame.pack_propagate(False)



def load_frame1():     
#______Podminky pro frame1
    def progressbar_iteration():
        while progressbar['value'] < 100:
            progressbar['value'] += 20
            time.sleep(0.1)
    def login_click():
        if j.get() =="michal" and h.get() !="heslo":
            h.delete(0,END)
            return h.insert(0,"spatne heslo")
        if j.get() !="michal" and h.get() == "heslo":
            j.delete(0,END)
            return j.insert(0,"spatne jmeno")
        if j.get() =="michal" and h.get() == "heslo":
            load_frame2()
            progressbar_iteration()
            
        if j.get() !="michal" and h.get() != "heslo":
            h.delete(0,END)
            j.delete(0,END)
            return (h.insert(0,"spatne heslo"),j.insert(0,"spatne jmeno"))
#_____konec podminek 
    #--------------------STRUKTURA frame1 ----------------------
    heading = Label(login_frame,text="Login System",font=("TkHeadingFont", 18),padx=20,pady=10)
    heading.grid(row=0,column=0,columnspan=2)
    
    jmeno_label = Label(login_frame,text="Uživatelske jmeno:",bg="#F0F0F8").grid(row=1,column=0)
    heslo_label = Label(login_frame,text="Heslo:",bg="#F0F0F8").grid(row=2,column=0)
    j = Entry(login_frame, width=30, border=10 )
    h = Entry(login_frame, width=30, border=10)#show="*"
    j.grid(row = 1,column = 1 ,padx = 20,pady = 10)
    h.grid(row = 2,column = 1,padx = 20,pady = 10)

    #definice tlacitka - prihlasit se
    login_button = Button(login_frame,
        text ="Login",
        font=("TkHeadingFont", 18),
        bg="#28393a",
        fg="white",
        padx=30,
        pady=15,
        command=login_click
        ).grid(row=3,column=0,columnspan=2)
    
    #definovani progressbaru------------
    progressbar = ttk.Progressbar(
        login_frame,
        orient='horizontal',
        mode='determinate',
        length=300)
    progressbar.grid(row=4,column=0,padx=20,pady=10,columnspan=2)
#---------------KONEC struktury frame1 -------------------------



#---------------ZACATEK FRAME2---------------------------
def load_frame2(): 
    

    accounts_frame.tkraise()
    add_acc = Button(accounts_frame,text="Přidej nový účet").pack
    view_acc = Button(accounts_frame,text="Zobraz existující účty").pack
    end_button = Button(accounts_frame,text="End the program").pack

#------------KONEC FRAME2---------------------------





#_________initializace aplikace__________
root = Tk()
root.title("Moje účty")
bg_color = "#3d6466"
root.eval("tk::PlaceWindow . center")
#_______vytvoreni frame widgetu_________
login_frame = Frame(root, bg=bg_color)
login_frame.pack()    
accounts_frame = Frame(root,bg=bg_color)
accounts_frame.pack()   #accounts_frame.grid(row=0,column=0)
load_frame1()
#for frame in (login_frame,accounts_frame):
#    frame.grid(row=0,column=0)



#_________run app____
root.mainloop()
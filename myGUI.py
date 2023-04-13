import customtkinter as ct
import time
from tkinter import ttk

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

def progressbar_iteration():
        progressbar.set(100)

def login_check():
    if jmeno_e.get()=="michal" and heslo_e.get()=="heslo":
        print("spravne")
        progressbar_iteration()
def slidebar_callback(value):
    progressbar.set(value)


root = ct.CTk()
root.geometry("400x350")        

frame1 = ct.CTkFrame(master=root)
frame1.grid(row=0,column=0)#expand=True,fill="both"
frame2 = ct.CTkFrame(master=root)
frame2.grid(row=1,column=0,)

label = ct.CTkLabel(frame1,text="Login system",font=(0,24))
label.pack(pady=12,padx=10)

jmeno_e = ct.CTkEntry(frame1,placeholder_text="jmeno")
heslo_e = ct.CTkEntry(frame1,placeholder_text="heslo",show="*")
for entry in (jmeno_e,heslo_e):
    entry.pack(pady=12,padx=10)

login_button = ct.CTkButton(frame1,text="Login",command=login_check)
login_button.pack(pady=12,padx=10)

progressbar = ct.CTkProgressBar(frame1,mode="determinate")
progressbar.pack(pady=12,padx=10)
slidebar = ct.CTkSlider(frame1,command=slidebar_callback).pack(pady=12,padx=10)



root.mainloop()
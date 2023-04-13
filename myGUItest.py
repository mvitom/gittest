import customtkinter 
import time


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

class LoginFrame(customtkinter.CTkFrame):
    def login_check(self):
            if self.jmeno_e.get()=="michal" and self.heslo_e.get()=="heslo":
                print("spravne")
                self.progressbar_iteration()
            else:
                print("spatne jmeno nebo heslo")
    def progressbar_iteration(self):
        while (self.progressbar.get())<100:
            self.progressbar.set(25)
            time.sleep(1)
            self.progressbar.set(50)
            time.sleep(1)
            self.progressbar.set(75)
            time.sleep(1)
            self.progressbar.set(100)

    def __init__(self, *args, header_name="LoginFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)
        self.jmeno_e = customtkinter.CTkEntry(self,placeholder_text="jmeno")
        self.jmeno_e.grid(row=1, column=0, padx=5, pady=10)
        self.heslo_e = customtkinter.CTkEntry(self,placeholder_text="heslo",show="*")
        self.heslo_e.grid(row=2, column=0, padx=5, pady=10)
        self.login_button = customtkinter.CTkButton(self,text="Login",command=self.login_check)
        self.login_button.grid(row=3, column=0, padx=5, pady=10)
        self.progressbar = customtkinter.CTkProgressBar(self,mode="determinate")
        self.progressbar.grid(row=4,column=0,padx=10,pady=(10,10))
        

class AccountsFrameEdit(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="AccountsFrameEdit", **kwargs):
        super().__init__(*args, **kwargs)
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name,width=400)
        self.header.grid(row=0, column=0, padx=10, pady=5)

class AccountsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="AccountsFrame", **kwargs):
        super().__init__(*args, **kwargs)
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name,width=400)
        self.header.grid(row=0, column=0, padx=10, pady=5)

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
        
        self.textbox.insert("0.0", "Some example text!\n" * 50)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x300")
        self.title("My Accounts app")

        self.login_frame = LoginFrame(self, header_name="LoginFrame")
        self.login_frame.grid(row=0, column=0, padx=20, pady=5)
        
        self.accounts_frame = AccountsFrame(self,header_name="AccountsFrame")
        self.accounts_frame.grid(row=0,column=1,padx=20,pady=20)
        # self.frame_1_button = customtkinter.CTkButton(self, text="Print value of frame 1", command=self.print_value_frame_1)
        # self.frame_1_button.grid(row=1, column=0, padx=20, pady=10)
        #self.login_button = customtkinter.CTkButton(self,text="Login",command=self.login_check)
        #self.login_button.grid(row=1, column=0, padx=20, pady=10)



    
    # def print_value_frame_1(self):
    #     print(f"Frame 1 value: {self.radio_button_frame_1.get_value()}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
 
"""def progressbar_iteration():
        progressbar.set(25)
        time.sleep(0.1)
        progressbar.set(50)
        time.sleep(0.1)
        progressbar.set(75)
        time.sleep(0.1)
        progressbar.set(100)



def slidebar_callback(value):
    progressbar.set(value)


frame1 = ct.CTkFrame(master=root)
frame1.pack(padx=20,pady=20,expand=True,fill="both")



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

"""


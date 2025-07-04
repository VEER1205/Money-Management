import customtkinter as ctk
import database as db
import os,sys
from tkinter import messagebox,filedialog
from PIL import Image
import pandas as pd
import dns.resolver
import re,json

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        if not os.path.exists("theme.json"):
            self.theme_json()
        self.attributes("-topmost",True)
        self.theme = self.load_json()
        self.resizable(False,False)
        self.geometry("600x350")
        ctk.set_appearance_mode(self.theme["mode"])    
        ctk.set_default_color_theme(self.theme["theme"])
        self.title("Money Management")
        self.bind("")

        self.data = []
        self.uid = None

        self.main_frame =ctk.CTkFrame(self)
        self.main_frame.place(x=0, y=0, relwidth=1, relheight=1) 
        self.m = ctk.CTkFrame(master=self.main_frame,width=200,height=280, bg_color="transparent", fg_color="transparent", corner_radius=5)
        self.m.pack(expand=True, side="left", fill="y",padx = 5,pady = 5)
        self.content_frame = ctk.CTkFrame(master=self.main_frame,width=400,height=330, bg_color="transparent", fg_color="transparent", corner_radius=5,border_color="gray")
        self.content_frame.pack(side="right", expand=False, fill="y", padx=5, pady=5)

        # importing Images
        self.eye_open_path = os.path.join(os.path.dirname(__file__),'images/image.png')
        self.eye_closed_path = os.path.join(os.path.dirname(__file__),'images/eye-crossed.png')
        self.eye_open = ctk.CTkImage(light_image=Image.open(self.eye_open_path), size=(20, 20))
        self.eye_closed = ctk.CTkImage(light_image=Image.open(self.eye_closed_path), size=(20, 20))

        # Create Frame Object
        self.Login_Frame = login_frame(self,controller=self)
        self.Setting_Frame = setting_frame(self.m,controller=self)
        self.menu_Frame = menu_frame(self.m,controller=self)
        self.Book = book(self.content_frame,controller=self)
        self.Add_Frame = add_frame(self.content_frame,controller=self)
        self.Remove_Frame = remove_frame(self.content_frame,controller=self)
        self.Singup_Frame = singup_frame(self,controller=self)
        self.place_frame()
        self.menu_Frame.mess.lift()
        self.show_frame(self.Book)
        self.show_frame(self.menu_Frame)
        self.show_frame(self.Login_Frame)

    def change_json(self,data)->None:
        with open("theme.json","+w") as file:
            json.dump(data,file,indent= 4)  

    def theme_json(self)->None:
        with open("theme.json","+w") as file:
            json.dump({"theme":"themes/rime.json","mode":"system"},file,indent= 4)         

    def load_json(self)->dict:
        with open("theme.json","r") as file:
            data = json.load(file)
        return data           
          
    def login(self)->None:
        if self.Login_Frame.login_id.get() == "" or self.Login_Frame.password.get() == "":
           pass
        else:
            self.uid = db.get_user(self.Login_Frame.login_id.get(), self.Login_Frame.password.get())
            if self.uid:
                 
                self.data = db.load_data(self.uid)  # Load user data after login
                self.update()
                self.main_frame.lift()
            else:
                if db.user_exists(self.Login_Frame.login_id.get()):
                    self.Login_Frame.login_mess.configure(text="Wrong Password!", font=("Roboto", 15, "bold"))
                else:
                    self.Login_Frame.login_mess.configure(text="No account found!", font=("Roboto", 15, "bold"))

    def New_user(self)->None:
        if self.Singup_Frame.login_id.get() == "" or self.Singup_Frame.password.get() == "":
            pass
        else:
            db.create_user(self.Singup_Frame.login_id.get(),self.Singup_Frame.password.get(),self.Singup_Frame.email.get())
            self.Login_Frame.lift()
            self.Login_Frame.login_mess.configure(text="Account created successfully!", font=("Roboto", 15, "bold"))
            self.Login_Frame.login_id.delete(0,"end")
            self.Login_Frame.password.delete(0,"end")
            self.reset_signup()

    def show_password(self,Frame)->None:
        if Frame.password.cget("show") == "*":
            Frame.password.configure(show="",font = ("Roboto", 15,"bold"))
            Frame.show.configure(image=self.eye_closed)  
        else:
            Frame.password.configure(show="*",font = ("Roboto", 20,"bold"))
            Frame.show.configure(image=self.eye_open)

    def place_frame(self)->None:
        for frame in (self.Book,self.Add_Frame,self.Remove_Frame,self.menu_Frame,self.Setting_Frame,self.Singup_Frame):
            frame.place(x=0,y = 0, relwidth=1, relheight=1)
            frame.pack_propagate(False)

    def show_frame(self,frame)->None:
        if frame in [self.Book,self.Add_Frame,self.Remove_Frame]:
            self.menu_Frame.mess.configure(text = "Welcome\nTo\nApp",font = ("Roboto", 20,"bold"))  
        frame.lift()  

    def update(self)->None:
        # Remove only old data (skip headers)
        for widget in self.Book.winfo_children()[3:]:
            widget.destroy()

    # Ensure headers are only created once
        if not self.Book.winfo_children():
            ctk.CTkLabel(self.Book, width=40, height=30, corner_radius=5, fg_color="gray", text="In.").grid(row=0, column=0, padx=2, sticky="w")
            ctk.CTkLabel(self.Book, width=210, height=30, corner_radius=5, fg_color="gray", text="Details").grid(row=0, column=1, padx=2, sticky="w")
            ctk.CTkLabel(self.Book, width=90, height=30, corner_radius=5, fg_color="gray", text="Amount").grid(row=0, column=2, padx=2, sticky="w")
        total_amount = 0
        for i, (en, am) in enumerate(self.data):
            ctk.CTkLabel(self.Book, width=40, height=30, text=i+1).grid(row=i+1, column=0, padx=2)
            ctk.CTkLabel(self.Book, width=210, height=30, text=en, anchor="w",wraplength=150).grid(row=i+1, column=1, padx=2)
            ctk.CTkLabel(self.Book, width=90, height=30, text=round(am,2), anchor="e").grid(row=i+1, column=2, padx=2) 
            self.Book.grid_rowconfigure(i+1, weight=0)
            total_amount += float(am)

        balance = f"Balance = {round(total_amount,2)}"
        self.menu_Frame.total.configure(text = f"Balance = {round(total_amount,2)}")
        # print(len(balance))
        # if len(balance) <= 20:
        #     self.menu_Frame.total.configure(text = balance)     
        # else:
        #     self.menu_Frame.total.configure(text = f"Balance\n=\n{round(total_amount,2)}") 

    def remove(self)->None:
        if self.Remove_Frame.index_in.get() == "":
            self.menu_Frame.mess.configure(text = "Pls Enter\nIndex",font = ("Roboto", 20,"bold"))
            self.focus()   
        else:
            try:
                e,m = self.data[int(self.Remove_Frame.index_in.get())-1]
                for widget in self.Remove_Frame.table.winfo_children()[2:]:
                    widget.destroy()
                ctk.CTkLabel(self.Remove_Frame.table, width=250, height=28, corner_radius=5 , text=e,anchor="w").grid(row = 1,column = 0,padx =5,pady =1)
                ctk.CTkLabel(self.Remove_Frame.table, width=105, height=28, corner_radius=5, text=m,anchor="e").grid(row = 1,column = 1,padx = 0,pady = 1)                
                db.delet_data(self.uid,e)
                del self.data[int(self.Remove_Frame.index_in.get())-1]
                self.menu_Frame.mess.configure(text = "Entry Removed!",font=("Roboto", 23,"bold"))
                self.update()
                self.Remove_Frame.index_in.delete(0,"end") 
                self.focus()
            except:
                self.menu_Frame.mess.configure(text = "Invalid\nSelection!",font = ("Roboto", 20,"bold"))
                self.Remove_Frame.index_in.delete(0,"end") 
                self.focus() 
                
    def Check_not_empty(self)->None:
        if self.Add_Frame.entery.get() == "" or self.Add_Frame.amount.get() == "":
            self.Add_Frame.empty.lift()
            self.focus()    
        else:
            try:
                if self.Add_Frame.cke.get():
                    self.data.Append(tuple([self.Add_Frame.entery.get().title(),float(self.Add_Frame.amount.get())]))
                    db.add_data(self.uid,self.Add_Frame.entery.get().title(),float(self.Add_Frame.amount.get()))
                else:    
                    self.data.Append(tuple([self.Add_Frame.entery.get().title(),-float(self.Add_Frame.amount.get())]))  
                    db.add_data(self.uid,self.Add_Frame.entery.get().title(),-float(self.Add_Frame.amount.get()))  
                self.Add_Frame.amount.delete(0,"end")
                self.Add_Frame.entery.delete(0,"end")  
                self.Add_Frame.cke.deselect()  
                self.Add_Frame.add_mess.lift()
                self.update()
                self.focus()
            except:
                self.Add_Frame.add_error.lift()
                self.focus() 

    def logout(self)->None:
        self.ask =  messagebox.askyesno("","Do You want to Logout")
        if self.ask:
            self.Login_Frame.login_id.delete(0,"end")
            self.Login_Frame.password.delete(0,"end")
            self.Login_Frame.login_mess.configure(text = "")
            self.show_frame(self.Login_Frame)
            self.show_frame(self.menu_Frame)                   

    def Delete_user(self)->None:
        ask =  messagebox.askyesno("","Do You want to Delete Account")
        if ask:
            db.delet_user(self.uid)
            self.Login_Frame.login_mess.configure(text="Account Deleted successfully!", font=("Roboto", 15, "bold"))
            self.Login_Frame.login_id.delete(0,"end")
            self.Login_Frame.password.delete(0,"end")
            self.show_frame(self.Login_Frame)
            self.show_frame(self.menu_Frame)  

    def export(self)->None:
        df = pd.DataFrame(data = self.data,columns=("Details","Amount"))
        df.index = range(1, len(df)+1)
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filepath:
            df.to_excel(filepath, index=False)  

    def import_data(self)->None:
        path = filedialog.askopenfilename(defaultextension=".xlsx",filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if path:
            try:
                df1 = pd.read_excel(path)
                df = df1[["Details", "Amount"]].values.tolist()
                data_list = list(map(tuple, df))

                #Check if the imported data has the correct structure
                if all(len(item) == 2 for item in data_list[1:]) and (data_list not in self.data):
                    self.data.extend(data_list[1:])
                    db.add_data_multiple(self.uid,self.data)
                    self.update()
                    self.show_frame(self.menu_Frame)
                else:
                    messagebox.showerror("Import Error","The imported data must have two columns(Details, Amount)")
            except Exception as e:
                messagebox.showerror("Import Error",f"Error importing data: {str(e)}")    

    def restart_App(self):
        """Restart the Application without closing the terminal."""
        self.python = sys.executable  # Get the Python interpreter path
        os.execl(self.python, self.python, *sys.argv)  # Restart the script   

    def is_valid_email(self,email)->str:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def domain_has_mx(self,domain)->bool:
        try:
            records = dns.resolver.resolve(domain, 'MX')
            return len(records) > 0
        except:
            return False

    def check_email(self,email)->None:
        if not self.is_valid_email(email):
            self.Singup_Frame.email_lable.configure(text = "Email ID: Invalid")
            self.Singup_Frame.email.configure(border_color = "red")
            return 
        domain = email.split('@')[1]
        if not self.domain_has_mx(domain):
            self.Singup_Frame.email_lable.configure(text = "Email ID: Invalid")
        self.Singup_Frame.email_lable.configure(text = "Email ID:")  
        self.Singup_Frame.email.configure(border_color = "gray")   

    def vaild_user(self)->None:
        if db.user_exists(self.Singup_Frame.login_id.get()):
            self.Singup_Frame.login_id_lable.configure(text="Account already exists!", font=("Roboto", 13, "bold")) 
            return
        self.Singup_Frame.login_id_lable.configure(text="Login ID:", font=("Roboto", 15, "bold"))

    def reset_signup(self)->None:
        self.Singup_Frame.login_id.delete(0,"end")
        self.Singup_Frame.email.delete(0,"end")
        self.Singup_Frame.password.delete(0,"end")
        self.Singup_Frame.login_id_lable.configure(text="Login ID:", font=("Roboto", 15, "bold"))    
        self.Singup_Frame.email_lable.configure(text = "Email ID:")  
        self.Singup_Frame.email.configure(border_color = "#565b5e") 
        self.focus()

    def change_themes(self,t)->None:
        self.theme["mode"] = t
        self.change_json(self.theme)
        ctk.set_appearance_mode(self.theme["mode"])  

    def change_color(self,c)->None:
        self.theme["theme"] = f"themes/{c}.json"
        self.change_json(self.theme)
        ctk.set_default_color_theme(self.theme["theme"])    
                    
class login_frame(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.controller = controller
        self.place(x = 0,y = 0,relwidth = 1,relheight = 1)

        self.login_page = ctk.CTkFrame(master = self,width=250,height=300,border_width=2,border_color="gray",fg_color="transparent")
        self.login_page.place(rely = 0.5,relx = 0.5,anchor = "center")

        self.login_lable = ctk.CTkLabel(master=self,text="Login",font=("Roboto", 35,"bold"))
        self.login_lable.place(relx=0.5, rely=0.07, anchor="center")

        self.login_mess = ctk.CTkLabel(master=self.login_page,text="",text_color="gray",font=("Roboto", 15,"bold"),width=150,height=30)
        self.login_mess.place(relx=0.5, rely=0.1, anchor="center")

        ctk.CTkLabel(master=self.login_page,text = "Login ID: ",font=("Roboto", 15,"bold")).place(relx=0.24, rely=0.19, anchor="center")
        self.login_id = ctk.CTkEntry(master=self.login_page,width=200,height=40,placeholder_text="",placeholder_text_color="gray70",font=("Roboto", 15,"bold"),justify="center")
        self.login_id.place(relx=0.5, rely=0.30, anchor="center") 

        ctk.CTkLabel(master=self.login_page,text = "Password: ",font=("Roboto", 15,"bold")).place(relx=0.24, rely=0.425, anchor="center")
        self.password = ctk.CTkEntry(master=self.login_page,width=170,height=40,placeholder_text="",show = "*",font=("Roboto", 15,"bold"),justify="center")
        self.password.place(relx=0.44, rely=0.55, anchor="center")

        self.login_button = ctk.CTkButton(master=self.login_page,text="Login",width=100,height=30,border_color="gray",corner_radius=5,command=lambda:(self.controller.login()),font=("Roboto", 15,"bold"))
        self.login_button.place(relx=0.5, rely=0.7142, anchor="center")

        self.new_user = ctk.CTkButton(master=self.login_page,text="Register",width=85,height=35,border_color="gray",corner_radius=5,command=lambda:(self.controller.show_frame(self.controller.Singup_Frame)),font=("Roboto", 15,"bold"),fg_color="transparent")
        self.new_user.place(relx=0.5, rely=0.85, anchor="center") 

        self.show = ctk.CTkButton(master= self.login_page,text="",image=self.controller.eye_open,fg_color="transparent",hover_color="#333333",width=20,height=20,command=lambda: self.controller.show_password(self.controller.Login_Frame))
        self.show.place(relx=.95, rely=0.54, anchor="e") 

class singup_frame(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.controller = controller

        self.login_page = ctk.CTkFrame(master = self,width=450,height=300,border_width=2,border_color="gray",fg_color="transparent")
        self.login_page.place(rely = 0.5,relx = 0.5,anchor = "center")

        self.login_lable = ctk.CTkLabel(master=self,text="Sign Up",font=("Roboto", 35,"bold"))
        self.login_lable.place(relx=0.5, rely=0.07, anchor="center")

        self.signup_mess = ctk.CTkLabel(master=self.login_page,text="",text_color="gray",font=("Roboto", 20,"bold"),width=150,height=35,anchor="center")
        self.signup_mess.place(relx = 0.6,rely = 0.1)

        self.email_lable = ctk.CTkLabel(self.login_page,text = "Email ID:",font=("Roboto", 15,"bold"),bg_color="transparent")
        self.email_lable.place(relx = 0.05,rely = 0.1)
        self.email = ctk.CTkEntry(master=self.login_page,width=180,height=40,placeholder_text="",placeholder_text_color="gray70",font=("Roboto", 15,"bold"),justify="center")
        self.email.place(relx=0.25, rely=0.25, anchor="center")
        self.email.bind("<FocusOut>",lambda ev:self.controller.check_email(self.email.get()))

        self.login_id_lable = ctk.CTkLabel(self.login_page,text = "Login ID:",font=("Roboto", 15,"bold"),bg_color="transparent",fg_color="transparent")
        self.login_id_lable.place(relx = 0.05,rely = 0.35)
        self.login_id = ctk.CTkEntry(master=self.login_page,width=180,height=40,placeholder_text="",placeholder_text_color="gray70",font=("Roboto", 15,"bold"),justify="center")
        self.login_id.place(relx=0.25, rely=0.50, anchor="center")
        self.login_id.bind("<FocusOut>",lambda ev:self.controller.vaild_user())

        ctk.CTkLabel(self.login_page,text = "Password:",font=("Roboto", 15,"bold"),bg_color="transparent",fg_color="transparent").place(relx = 0.05,rely = 0.6)
        self.password = ctk.CTkEntry(master=self.login_page,width=180,height=40,placeholder_text="",show = "*",font=("Roboto", 20,"bold"))
        self.password.place(relx=0.25, rely=0.75, anchor="center")

        self.show = ctk.CTkButton(master= self.login_page,text="",image=self.controller.eye_open,bg_color="#343638",fg_color="#343638",width=20,height=20,command=lambda: (self.controller.show_password(self.controller.Singup_Frame)))
        self.show.place(relx=.43, rely=0.75, anchor="e") 

        self.register_button = ctk.CTkButton(self.login_page,width=150,height=35,text="Sign Up",font=("Roboto",20,"bold"),command=lambda:self.controller.New_user())
        self.register_button.place(relx = 0.6,rely = 0.3)

        self.login_button = ctk.CTkButton(self.login_page,width=150,height=35,text="Login",font=("Roboto",20,"bold"),command=lambda:(self.controller.show_frame(self.controller.Login_Frame),self.controller.reset_signup()))
        self.login_button.place(relx = 0.6,rely = 0.5)

        ctk.CTkFrame(self.login_page,width=5,height=260,border_width=1,corner_radius=0,bg_color="gray",border_color="gray",fg_color="gray").place(rely = 0.5,relx = 0.53,anchor = "center")
        
class setting_frame(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master,corner_radius=5,border_width=3)
        self.controller = controller
    
        home_i_path = os.path.join(os.path.dirname(__file__),'images/home.png')
        home_i = ctk.CTkImage(light_image=Image.open(home_i_path), size=(20, 20))

        home_button = ctk.CTkButton(master=self,text="",image=home_i,height= 20,width=20,command= lambda : self.controller.show_frame(self.controller.menu_Frame))
        home_button.place(relx = 0.05, rely = 0.02)

        delete_buttom = ctk.CTkButton(master=self, text="Delete Account", command=lambda:(self.controller.Delete_user()))
        delete_buttom.pack(side = "bottom",pady = 10,padx = 10)

        logout_buttom = ctk.CTkButton(master=self, text="Logout", command=lambda:self.controller.logout())
        logout_buttom.pack(side = "bottom",pady = 1,padx = 10)

        export_button = ctk.CTkButton(master=self,text="Export to xlsx",command=lambda :self.controller.export())
        export_button.pack(side = "bottom",pady = 10,padx = 10)

        import_button = ctk.CTkButton(master=self,text="Import Data",command=lambda :self.controller.import_data())
        import_button.pack(side = "bottom",pady = 1,padx = 10)

        theme_button = ctk.CTkOptionMenu(master=self,values=["light","dark","system"],command=self.controller.change_themes)
        theme_button.pack(side = "bottom",pady = 10,padx = 10)
        theme_button.set("theme")
        
        color_button =theme_button = ctk.CTkOptionMenu(master=self,values=["marsh","orange","rime"],command=self.controller.change_color)
        color_button.pack(side = "bottom",pady = 1,padx = 10)
        color_button.set("color")
        
class menu_frame(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master,border_width=3,corner_radius=5)
        self.controller = controller

        self.sett_i_path = os.path.join(os.path.dirname(__file__), 'images/setting.png')
        self.sett_i = ctk.CTkImage(light_image=Image.open(self.sett_i_path), size=(20, 20))
        self.setting_button = ctk.CTkButton(master=self,text="",image=self.sett_i,height= 20,width=20,command= lambda : self.controller.show_frame(self.controller.Setting_Frame))
        self.setting_button.place(relx = 0.05, rely = 0.02)

        self.mess = ctk.CTkLabel(master=self,text="Welcome\nTo\nApp",width=185,height=80,font=("Roboto", 23,"bold"),fg_color="transparent",bg_color="transparent")
        self.mess.place(relx = 0.5,rely=0.25, anchor="center")

        self.total = ctk.CTkLabel(master = self,text="Balance = 0",anchor="w",height=30,font=("Roboto", 17,"bold"))
        self.total.place(relx=0.5, rely=0.58, anchor="center")
        self.total.lift()

        ctk.CTkButton(master=self,text="Add Entery",command=lambda:(self.controller.show_frame(self.controller.Add_Frame),self.mess.lift())).pack(pady = 10,side = "bottom")
        ctk.CTkButton(master=self,text="Remove Entery",command=lambda:(self.controller.show_frame(self.controller.Remove_Frame),self.mess.lift())).pack(pady = 0,side = "bottom")
        ctk.CTkButton(master=self,text="Show Entery",command=lambda:(self.controller.show_frame(self.controller.Book),self.mess.lift())).pack(pady = 10,side = "bottom")

class book(ctk.CTkScrollableFrame):
    def __init__(self, master,controller):
        super().__init__(master,border_width=3,orientation="vertical",corner_radius=5)
        self.controller = controller
        
        ctk.CTkButton(self, width=40, height=30,corner_radius=5,text="In.",state="disable").grid(row = 0,column = 0,padx = 1,pady = 0)
        ctk.CTkButton(self,width=210, height=30,corner_radius=5,  text="Details",state="disable").grid(row = 0,column = 1,padx = 1,pady = 0)
        ctk.CTkButton(self,width=90, height=30, corner_radius=5, text="Amount",state="disable").grid(row = 0,column = 2,padx = 1,pady = 0)

class add_frame(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master,corner_radius=5,border_width=3)
        self.controller = controller

        self.add_mess = ctk.CTkLabel(master=self.controller.menu_Frame,text="Entry Added!",width=185,height=120,font=("Roboto", 23,"bold"),text_color="green")
        self.add_mess.place(relx = 0.5,rely=0.35, anchor="center")

        self.add_error = ctk.CTkLabel(master=self.controller.menu_Frame,text="INVALIDE\nINPUT",width=185,height=120,font=("Roboto", 23,"bold"),)
        self.add_error.place(relx = 0.5,rely=0.35, anchor="center")

        self.empty = ctk.CTkLabel(master=self.controller.menu_Frame,text="Pls Enter The\nDetials",width=185,height=120,font=("Roboto", 23,"bold"),)
        self.empty.place(relx = 0.5,rely=0.35, anchor="center")

        self.entery = ctk.CTkEntry(self,placeholder_text="Enter The Entery",width=200,height=50,font=("Roboto", 20,"bold"),justify="center")
        self.entery.place(x = 100,y = 70,)

        self.amount = ctk.CTkEntry(self,placeholder_text = "Enter The Amount",width=150,height=40,font=("Roboto", 13,"bold"),justify="center")
        self.amount.place(x = 123,y = 140)

        self.cke = ctk.CTkCheckBox(self,width=40,height=40,checkbox_height=20,checkbox_width=20,text="IF CASH IS ADD")
        self.cke.place(x = 136,y = 190)

        self.sumbmit = ctk.CTkButton(self,width=100,height=30,text="Add",command= lambda:self.controller.Check_not_empty())
        self.sumbmit.place(x = 145,y = 240)

class remove_frame(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master,corner_radius=5,border_width=1)
        self.controller = controller

        self.table = ctk.CTkFrame(master=self,border_width=1,height=100)
        self.table.pack(expand = True,fill = "both",pady = 5,padx = 3)
        self.table.pack_propagate(False) 

        self.menu = ctk.CTkFrame(master=self,height=250)
        self.menu.pack(fill = "both", padx = 3,pady = 5)
        self.menu.pack_propagate(False)

        self.index = ctk.CTkLabel(master = self.menu,text="Enter The Index For Remove The Entery",height=50,font = ("Roboto", 15,"bold"))
        self.index.pack(side = "top",padx = 10,pady =15)

        self.index_in = ctk.CTkEntry(self.menu,width=80,height=30,placeholder_text="Enter",font=("Roboto", 20,"bold"),justify="center")
        self.index_in.pack(side = "top",padx = 10,pady = 10)

        self.delet = ctk.CTkButton(self.menu,text="Remove",command= lambda:self.controller.remove()).pack()

        ctk.CTkButton(self.table, width=250, height=28, corner_radius=5,  text="Details",state="disable").grid(row = 0,column = 0,padx =5,pady =4)
        ctk.CTkButton(self.table, width=105, height=28, corner_radius=5,  text="Amount",state="disable").grid(row = 0,column = 1,padx = 0,pady =4)

if __name__ == "__main__":
    App = App()
    App.mainloop()
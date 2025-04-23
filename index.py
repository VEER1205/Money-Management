import customtkinter as ctk
import database as db
import os,sys
from tkinter import messagebox,filedialog
from PIL import Image
import pandas as pd

ctk.set_appearance_mode("system")
if __name__ == "__main__":
    app = ctk.CTk()
    ctk.set_default_color_theme("themes/marsh.json")
    app.title("Money Management")
    main_frame = ctk.CTkFrame(master=app) 
    main_frame.place(x=0, y=0, relwidth=1, relheight=1)
    a = []

# Main Frame  
    m = ctk.CTkFrame(master=main_frame,width=200,height=280, bg_color="transparent", fg_color="transparent", corner_radius=5)
    m.pack(expand=True, side="left", fill="y",padx = 5,pady = 5) 

    content_frame = ctk.CTkFrame(master=main_frame,width=400,height=330, bg_color="transparent", fg_color="transparent", corner_radius=5,border_color="gray")
    content_frame.pack(side="right", expand=False, fill="y", padx=5, pady=5)
        
    main = ctk.CTkFrame(master=m,fg_color="#333333",corner_radius=5)
    main.place(x = 0, y = 0, relwidth=1, relheight=1 )

    mess = ctk.CTkLabel(master=main,text="Welcome\nTo\nApp",width=185,height=120,font=("Roboto", 23,"bold"),)
    mess.place(relx = 0.5,rely=0.35, anchor="center")

    total = ctk.CTkLabel(master = main,text="Balance = 0",anchor="w",height=30,font=("Roboto", 17,"bold"))
    total.place(relx=0.5, rely=0.58, anchor="center") 

# setting 
    setting = ctk.CTkFrame(master=m, bg_color="transparent", fg_color="#333333", corner_radius=5)
    setting.place(x = 0, y = 0, relwidth=1, relheight=1 )
    sett_i_path = os.path.join(os.path.dirname(__file__), 'images/setting.png')
    home_i_path = os.path.join(os.path.dirname(__file__),'images/home.png')
    sett_i = ctk.CTkImage(light_image=Image.open(sett_i_path), size=(20, 20))
    home_i = ctk.CTkImage(light_image=Image.open(home_i_path), size=(20, 20))

    setting_button = ctk.CTkButton(master=main,text="",image=sett_i,height= 20,width=20,command= lambda : show_frame(setting))
    setting_button.place(relx = 0.05, rely = 0.02)

    home_button = ctk.CTkButton(master=setting,text="",image=home_i,height= 20,width=20,command= lambda : show_frame(main))
    home_button.place(relx = 0.05, rely = 0.02)

    delete_buttom = ctk.CTkButton(master=setting, text="Delete Account", command=lambda:Delete_user())
    delete_buttom.pack(side = "bottom",pady = 10,padx = 10)

    logout_buttom = ctk.CTkButton(master=setting, text="Logout", command=lambda:logout())
    logout_buttom.pack(side = "bottom",pady = 1,padx = 10)

    export_button = ctk.CTkButton(master=setting,text="Export to xlsx",command=lambda :export())
    export_button.pack(side = "bottom",pady = 10,padx = 10)

    import_button = ctk.CTkButton(master=setting,text="Import Data",command=lambda :import_data(a))
    import_button.pack(side = "bottom",pady = 1,padx = 10)

    

# Login Frame
    login_frame = ctk.CTkFrame(master=app)
    login_frame.place(x=0, y=0, relwidth=1, relheight=1)

    login_id = ctk.CTkEntry(master=login_frame,width=150,height=30,placeholder_text="Enter The ID",font=("Roboto", 15,"bold"),justify="center")
    login_id.place(relx=0.5, rely=0.35, anchor="center") 
    
    eye_open_path = os.path.join(os.path.dirname(__file__),'images/image.png')
    eye_closed_path = os.path.join(os.path.dirname(__file__),'images/eye-crossed.png')
    eye_open = ctk.CTkImage(light_image=Image.open(eye_open_path), size=(20, 20))
    eye_closed = ctk.CTkImage(light_image=Image.open(eye_closed_path), size=(20, 20))

    login_mess = ctk.CTkLabel(master=login_frame,text="",font=("Roboto", 15,"bold"),width=150,height=30)
    login_mess.place(relx=0.5, rely=0.25, anchor="center") 

    login_button = ctk.CTkButton(master=login_frame,text="Login",width=60,height=30,border_color="gray",corner_radius=5,command=lambda:(login()),font=("Roboto", 15,"bold"))
    login_button.place(relx=0.42, rely=0.65, anchor="center") 

    password = ctk.CTkEntry(master=login_frame,width=150,height=30,placeholder_text="PASSWORD",show = "*",font=("Roboto", 15,"bold"),justify="center")
    password.place(relx=0.5, rely=0.5, anchor="center")

    new_user = ctk.CTkButton(master=login_frame,text="Sign Up",width=60,height=30,border_color="gray",corner_radius=5,command=lambda:(New_user()),font=("Roboto", 15,"bold"))
    new_user.place(relx=0.57, rely=0.65, anchor="center") 

    show = ctk.CTkButton(master= login_frame,text="",image=eye_open,fg_color="transparent",hover_color="#333333",width=20,height=30,command=lambda: show_password())
    show.place(relx=0.66, rely=0.5, anchor="center") 


# For Adding The Entery 

    add_f = ctk.CTkFrame(master=content_frame, bg_color="transparent", fg_color="#333333", corner_radius=5)

    add_mess = ctk.CTkLabel(master=main,text="Entry Added!",width=185,height=120,font=("Roboto", 23,"bold"),text_color="green")
    add_mess.place(relx = 0.5,rely=0.35, anchor="center")

    add_error = ctk.CTkLabel(master=main,text="INVALIDE\nINPUT",width=185,height=120,font=("Roboto", 23,"bold"),)
    add_error.place(relx = 0.5,rely=0.35, anchor="center")

    empty = ctk.CTkLabel(master=main,text="Pls Enter The\nDetials",width=185,height=120,font=("Roboto", 23,"bold"),)
    empty.place(relx = 0.5,rely=0.35, anchor="center")

    entery = ctk.CTkEntry(add_f,placeholder_text="Enter The Entery",width=200,height=50,font=("Roboto", 20,"bold"),justify="center")
    entery.place(x = 100,y = 70,)

    amout = ctk.CTkEntry(add_f,placeholder_text = "Enter The Amount",width=150,height=40,font=("Roboto", 13,"bold"),justify="center")
    amout.place(x = 123,y = 140)

    cke = ctk.CTkCheckBox(add_f,width=40,height=40,checkbox_height=20,checkbox_width=20,text="IF CASH IS ADD")
    cke.place(x = 136,y = 190)

    sumbmit = ctk.CTkButton(add_f,width=100,height=30,text="Add",command= lambda:Check_not_empty())
    sumbmit.place(x = 145,y = 240)


# For removing The Entery

    remove_F = ctk.CTkFrame(master=content_frame, bg_color="#333333",fg_color="#333333",corner_radius=10)
    
    table = ctk.CTkFrame(master=remove_F,border_width=1,border_color="gray",height=100)
    table.pack(expand = True,fill = "both",pady = 5,padx = 3)
    table.pack_propagate(False) 

    manu = ctk.CTkFrame(master=remove_F,height=250)
    manu.pack(fill = "both", padx = 3,pady = 5)
    manu.pack_propagate(False)

    index = ctk.CTkLabel(master = manu,text="Enter The Index For Remove The Entery",height=50,font = ("Roboto", 15,"bold"))
    index.pack(side = "top",padx = 10,pady =15)

    index_in = ctk.CTkEntry(manu,width=80,height=30,placeholder_text="Enter",font=("Roboto", 20,"bold"),justify="center")
    index_in.pack(side = "top",padx = 10,pady = 10)

    delet = ctk.CTkButton(manu,text="Remove",command= lambda:remove()).pack()

    ctk.CTkLabel(table, width=250, height=28, corner_radius=5, fg_color="gray", text="Details").grid(row = 0,column = 0,padx =5,pady =4)
    ctk.CTkLabel(table, width=105, height=28, corner_radius=5, fg_color="gray", text="Amount").grid(row = 0,column = 1,padx = 0,pady =4)



# For Viwe All Entery

    book = ctk.CTkScrollableFrame(master=content_frame,bg_color="#333333",fg_color="#333333",border_color="gray",border_width=1,scrollbar_button_color="#333333")
    ctk.CTkLabel(book, width=40, height=30, corner_radius=5, fg_color="gray", text="In.").grid(row = 0,column = 0,padx = 2,pady = 0)
    ctk.CTkLabel(book, width=210, height=30, corner_radius=5, fg_color="gray", text="Details").grid(row = 0,column = 1,padx = 2,pady =0)
    ctk.CTkLabel(book, width=90, height=30, corner_radius=5, fg_color="gray", text="Amount").grid(row = 0,column = 2,padx = 2,pady = 0)


# The Main Logic 

    for frame in (add_f, book, remove_F):
        frame.place(x=0,y = 0, relwidth=1, relheight=1)
    add_f.pack_propagate(False)
    book.pack_propagate(False)    
    
    def update():
        # Remove only old data (skip headers)
        for widget in book.winfo_children()[3:]:
            widget.destroy()

    # Ensure headers are only created once
        if not book.winfo_children():
            ctk.CTkLabel(book, width=40, height=30, corner_radius=5, fg_color="gray", text="In.").grid(row=0, column=0, padx=2, sticky="w")
            ctk.CTkLabel(book, width=210, height=30, corner_radius=5, fg_color="gray", text="Details").grid(row=0, column=1, padx=2, sticky="w")
            ctk.CTkLabel(book, width=90, height=30, corner_radius=5, fg_color="gray", text="Amount").grid(row=0, column=2, padx=2, sticky="w")
        total_amount = 0
        for i, (en, am) in enumerate(a):
            ctk.CTkLabel(book, width=40, height=30, text=i+1).grid(row=i+1, column=0, padx=2)
            ctk.CTkLabel(book, width=210, height=30, text=en, anchor="w",wraplength=180).grid(row=i+1, column=1, padx=2)
            ctk.CTkLabel(book, width=90, height=30, text=am, anchor="e").grid(row=i+1, column=2, padx=2) 
            total_amount += float(am)

        total.configure(text = f"Balance = {total_amount}")    
    
    def remove():
        if index_in.get() == "":
            mess.configure(text = "Pls Enter\nIndex",font = ("Roboto", 20,"bold"))
            app.focus()   
        else:
            try:
                e,m = a[int(index_in.get())-1]
                for widget in table.winfo_children()[2:]:
                    widget.destroy()
                ctk.CTkLabel(table, width=250, height=28, corner_radius=5 , text=e,anchor="w").grid(row = 1,column = 0,padx =5,pady =1)
                ctk.CTkLabel(table, width=105, height=28, corner_radius=5, text=m,anchor="e").grid(row = 1,column = 1,padx = 0,pady = 1)                
                db.delet_data(uid,e)
                del a[int(index_in.get())-1]
                mess.configure(text = "Entry Removed!",font=("Roboto", 23,"bold"))
                update()
                index_in.delete(0,"end") 
                app.focus()
            except:
                mess.configure(text = "Invalid\nSelection!",font = ("Roboto", 20,"bold"))
                index_in.delete(0,"end") 
                app.focus() 
                
    def Check_not_empty():
        if entery.get() == "" or amout.get() == "":
            empty.lift()
            app.focus()    
        else:
            try:
                if cke.get():
                    a.append(tuple([entery.get().title(),float(amout.get())]))
                    db.add_data(uid,entery.get().title(),float(amout.get()))
                else:    
                    a.append(tuple([entery.get().title(),-float(amout.get())]))  
                    db.add_data(uid,entery.get().title(),-float(amout.get()))  
                amout.delete(0,"end")
                entery.delete(0,"end")  
                cke.deselect()  
                add_mess.lift()
                update()
                app.focus()
            except:
                add_error.lift()
                app.focus()

    def show_frame(frame):
        if frame in [add_f,remove_F,book]:
            mess.configure(text = "Welcome\nTo\nApp",font = ("Roboto", 20,"bold"))
        frame.lift()
        
    ctk.CTkButton(master=main,text="Add Entery",command=lambda:(show_frame(add_f),mess.lift()),).pack(pady = 10,side = "bottom")
    ctk.CTkButton(master=main,text="Remove Entery",command=lambda:(show_frame(remove_F),mess.lift()),).pack(pady = 0,side = "bottom")
    ctk.CTkButton(master=main,text="Show Entery",command=lambda:(show_frame(book),mess.lift()),).pack(pady = 10,side = "bottom")
    show_frame(book)

    def show_password():
        if password.cget("show") == "*":
            password.configure(show="")
            show.configure(image=eye_closed)  
        else:
            password.configure(show="*")
            show.configure(image=eye_open)

    def logout():
        ask =  messagebox.askyesno("","Do You want to Logout")
        if ask:
            login_id.delete(0,"end")
            password.delete(0,"end")
            login_frame.lift()
            main.lift()
        
    def login():
        global uid  
        if login_id.get() == "" or password.get() == "":
           pass
        else:
            uid = db.get_user(login_id.get(), password.get())
            if uid:
                global a  
                a = db.load_data(uid)  # Load user data after login
                update()
                main_frame.lift()
            else:
                if db.user_exists(login_id.get()):
                    login_mess.configure(text="Wrong Password!", font=("Roboto", 15, "bold"))
                else:
                    login_mess.configure(text="No account found!", font=("Roboto", 15, "bold"))
   
    def New_user():
        if db.user_exists(login_id.get()):
            login_mess.configure(text="Account already exists!", font=("Roboto", 15, "bold"))
        
        elif login_id.get() == "" or password.get() == "":
            pass
        
        else:
            db.create_user(login_id.get(),password.get())
            login_mess.configure(text="Account created successfully!", font=("Roboto", 15, "bold"))
            login_id.delete(0,"end")
            password.delete(0,"end")

    def Delete_user():
        ask =  messagebox.askyesno("","Do You want to Delete Account")
        if ask:
            db.delet_user(uid)
            login_mess.configure(text="Account Deleted successfully!", font=("Roboto", 15, "bold"))
            login_id.delete(0,"end")
            password.delete(0,"end")
            login_frame.lift()
            main.lift()

    def export():
        df = pd.DataFrame(data = a,columns=("Details","Amount"))
        df.index = range(1, len(df)+1)
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filepath:
            df.to_excel(filepath, index=False)  
    
    def import_data(a):
        path = filedialog.askopenfilename(defaultextension=".xlsx",filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if path:
            try:
                df = pd.read_excel(path,header=None)
                data_list = list(map(tuple, df.values))

                #Check if the imported data has the correct structure
                if all(len(item) == 2 for item in data_list[1:]):
                    a.extend(data_list[1:])
                    update()
                    main.lift()
                else:
                    messagebox.showerror("Import Error","The imported data must have two columns(Details, Amount)")
            except Exception as e:
                messagebox.showerror("Import Error",f"Error importing data: {str(e)}")

    def restart_app():
        """Restart the application without closing the terminal."""
        python = sys.executable  # Get the Python interpreter path
        os.execl(python, python, *sys.argv)  # Restart the script

# Add a Restart Button in your UI
    btn_restart = ctk.CTkButton(master=setting, text="Restart App", command=restart_app)
    btn_restart.place(relx= 0.27 ,rely = 0.02)
    update()
    mess.lift()
    main.lift()
    app.geometry("600x350")
    app.resizable(False,False)
    app.attributes("-topmost", True)
    app.mainloop()
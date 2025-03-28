from customtkinter import CTk
from tkinter import ttk
import customtkinter as ctk
import os,sys

ctk.set_appearance_mode("system")
if __name__ == "__main__":
    app = ctk.CTk()
    main_frame = ctk.CTkFrame(master=app) 
    main_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Main Frame  
    a = [("Buy laptop",+1000000000),("Phone",-120000),("The Phone ,pc,car and laptop mac book ",1234567890)]
    
    main = ctk.CTkFrame(master=main_frame,width=195,height=280)
    main.pack(expand=False, side="left", fill="both",padx = 5,pady = 5) 
    content_frame = ctk.CTkFrame(master=main_frame,width=395,height=330)
    content_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)
    mess = ctk.CTkLabel(master=main,text="Welcome\nTo\nApp",width=185,height=185,font=("Roboto", 23,"bold"))
    mess.pack(expand = False,side = "top",padx = 10,pady = 7)
    # title = ctk.CTkLabel(content_frame,text = "TITLE",).pack(side = "top",padx = 10,pady = 10)

# Login Frame
    login_frame = ctk.CTkFrame(master=app)
    login_frame.place(x=0, y=0, relwidth=1, relheight=1)
    login_id = ctk.CTkEntry(master=login_frame,width=150,height=30,placeholder_text="Enter The ID",font=("Roboto", 15,"bold"),justify="center")
    login_id.place(x = 225,y =120)
    # login_pass = ctk.CTkEntry()
    login_bu = ctk.CTkButton(master=login_frame,text="Login",width=80,height=30,border_color="gray",corner_radius=10,command=lambda:login(),font=("Roboto", 20,"bold"))
    login_bu.pack(padx = 10,pady =100,side = "bottom")

# For Adding The Entery 
    add_f = ctk.CTkFrame(master=content_frame,fg_color="#333333",)
    entery = ctk.CTkEntry(add_f,placeholder_text="Enter The Entery",width=200,height=50,font=("Roboto", 20,"bold"),justify="center")
    entery.place(x = 100,y = 70,)
    amout = ctk.CTkEntry(add_f,placeholder_text = "Enter The Amount",width=150,height=40,font=("Roboto", 13,"bold"),justify="center")
    amout.place(x = 123,y = 140)
    cke = ctk.CTkCheckBox(add_f,width=40,height=40,checkbox_height=20,checkbox_width=20,text="IF CASH IS ADD")
    cke.place(x = 136,y = 190)
    sumbmit = ctk.CTkButton(add_f,width=100,height=30,text="Add",command= lambda:Check_not_empty())
    sumbmit.place(x = 145,y = 240)
    
# For removing The Entery
    remove_F = ctk.CTkFrame(master=content_frame)
    table = ctk.CTkFrame(master=remove_F,border_width=1,border_color="gray",height=100,width=200)
    table.pack(fill = "both",expand = True,pady = 5,padx = 3)
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
    book = ctk.CTkScrollableFrame(master=content_frame,bg_color="#333333",fg_color="#333333",border_color="gray",border_width=1)
    ctk.CTkLabel(book, width=40, height=30, corner_radius=5, fg_color="gray", text="In.").grid(row = 0,column = 0,padx = 2,pady = 0)
    ctk.CTkLabel(book, width=210, height=30, corner_radius=5, fg_color="gray", text="Details").grid(row = 0,column = 1,padx = 2,pady =0)
    ctk.CTkLabel(book, width=90, height=30, corner_radius=5, fg_color="gray", text="Amount").grid(row = 0,column = 2,padx = 2,pady = 0)
       
# The Main Logic 
    for frame in (add_f, book, remove_F):
        frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    def upadate():
        # Remove only old data (skip headers)
        for widget in book.winfo_children()[3:]:
            widget.destroy()

    # Ensure headers are only created once
        if not book.winfo_children():
            ctk.CTkLabel(book, width=40, height=30, corner_radius=5, fg_color="gray", text="In.").grid(row=0, column=0, padx=2, sticky="w")
            ctk.CTkLabel(book, width=210, height=30, corner_radius=5, fg_color="gray", text="Details").grid(row=0, column=1, padx=2, sticky="w")
            ctk.CTkLabel(book, width=90, height=30, corner_radius=5, fg_color="gray", text="Amount").grid(row=0, column=2, padx=2, sticky="w")
    
        for i, (en, am) in enumerate(a):
            ctk.CTkLabel(book, width=40, height=30, text=i+1).grid(row=i+1, column=0, padx=2)
            ctk.CTkLabel(book, width=210, height=30, text=en, anchor="w",wraplength=180).grid(row=i+1, column=1, padx=2)
            ctk.CTkLabel(book, width=90, height=30, text=am, anchor="e").grid(row=i+1, column=2, padx=2) 
    
    def remove():
        if index_in.get() == "":
            mess.configure(text = "Pls Enter\nIndex",font = ("Roboto", 20,"bold"))
            app.focus()   
        else:
            try:
                if int(index_in.get())<=0:
                    mess.configure(text = "INVALIDE\nINPUT",font = ("Roboto", 20,"bold"))
                    index_in.delete(0,"end") 
                    app.focus()
                else: 
                    e,m = a[int(index_in.get())-1]
                    for widget in table.winfo_children()[2:]:
                        widget.destroy()
                    ctk.CTkLabel(table, width=250, height=28, corner_radius=5 , text=e,anchor="w").grid(row = 1,column = 0,padx =5,pady =1)
                    ctk.CTkLabel(table, width=105, height=28, corner_radius=5, text=m,anchor="e").grid(row = 1,column = 1,padx = 0,pady = 1)                
                    del a[int(index_in.get())-1]
                    mess.configure(text = "Entry Removed!",font=("Roboto", 23,"bold"))
                    upadate()
                    index_in.delete(0,"end") 
                    app.focus()
            except:  
                mess.configure(text = "Invalid\nSelection!",font = ("Roboto", 20,"bold")) 
                index_in.delete(0,"end")  
                app.focus()

    def Check_not_empty():
        if entery.get() == "" or amout.get() == "":
            mess.configure(text = "Pls Enter The\nDetials",font = ("Roboto", 20,"bold"))
            app.focus()    
        else:
            try:
                if cke.get():
                    a.append(tuple([entery.get().title(),int(amout.get())]))
                else:    
                    a.append(tuple([entery.get().title(),-int(amout.get())]))    
                amout.delete(0,"end")
                entery.delete(0,"end")  
                cke.deselect()  
                mess.configure(text = "Entry Added!",font=("Roboto", 23,"bold"))
                upadate()
                app.focus()
            except:
                mess.configure(text = "INVALIDE\nINPUT",font = ("Roboto", 20,"bold"))

    def show_frame(frame):
        mess.configure(text = "Welcome\nTo\nApp",font = ("Roboto", 20,"bold"))
        frame.lift() 
    ctk.CTkButton(master=main,text="Add Entery",command=lambda:show_frame(add_f),).pack(pady = 10,side = "bottom")
    ctk.CTkButton(master=main,text="Remove Entery",command=lambda:show_frame(remove_F),).pack(pady = 0,side = "bottom")
    ctk.CTkButton(master=main,text="Show Entery",command=lambda:show_frame(book),).pack(pady = 10,side = "bottom")
    show_frame(remove_F)
    def logout():
        login_frame.lift()

    def login():
        main_frame.lift()    

    def restart_app():
        """Restart the application without closing the terminal."""
        python = sys.executable  # Get the Python interpreter path
        os.execl(python, python, *sys.argv)  # Restart the script
   
# Add a Restart Button in your UI
    btn_restart = ctk.CTkButton(master=main, text="Restart App", command=restart_app)
    btn_restart.place(x = 40,y =10)
    upadate()
    app.geometry("600x350")
    app.resizable(False,False)
    app.attributes("-topmost", True)
    app.mainloop()
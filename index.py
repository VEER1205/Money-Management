from customtkinter import CTk
from tkinter import ttk
import customtkinter as ctk
import os,sys

ctk.set_appearance_mode("system")
if __name__ == "__main__":
    app = ctk.CTk()
# Main Frame  
    a = [("Buy laptop",100000000),("Phone",120000)]
    main = ctk.CTkFrame(master=app,width=195,height=280)
    main.pack(expand=False, side="left", fill="both",padx = 5,pady = 5) 
    content_frame = ctk.CTkFrame(master=app,width=395,height=330)
    content_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)
    mess = ctk.CTkLabel(master=main,text="Welcome\nTo\nApp",width=185,height=185,font=("Roboto", 23,"bold"))
    mess.pack(expand = False,side = "top",padx = 10,pady = 5)
    # title = ctk.CTkLabel(content_frame,text = "TITLE",).pack(side = "top",padx = 10,pady = 10)


# For Adding The Entery 
    add_f = ctk.CTkFrame(master=content_frame)
    # add_f.pack(expand = False,side = "right",fill = "both",padx = 5,pady=5)
    entery = ctk.CTkEntry(add_f,placeholder_text="Enter The Entery",width=200,height=50,font=("Roboto", 20,"bold"),justify="center")
    entery.place(x = 100,y = 70,)
    amout = ctk.CTkEntry(add_f,placeholder_text = "Enter The Amount",width=150,height=40,font=("Roboto", 13,"bold"),justify="center")
    amout.place(x = 123,y = 140)
    def Check_not_empty():
        if entery.get() == "" or amout.get() == "":
            mess.configure(text = "Pls Enter The\nDetials",font = ("Roboto", 20,"bold"))
            app.focus()    
        else:
            amout.delete(0,"end")
            entery.delete(0,"end")    
            mess.configure(text = "Welcom\nTo\nApp",font=("Roboto", 23,"bold"))
            app.focus()


    sumbmit = ctk.CTkButton(add_f,width=100,height=30,text="Add",command= lambda:Check_not_empty())
    sumbmit.place(x = 145,y = 200)
    

# For removing The Entery
    remove_F = ctk.CTkFrame(master=content_frame)
    
    


# For Viwe All Entery
    book = ctk.CTkScrollableFrame(master=content_frame,)
    ctk.CTkLabel(book, width=40, height=30, corner_radius=5, fg_color="gray", text="In.").grid(row = 0,column = 0,padx = 2)
    ctk.CTkLabel(book, width=210, height=30, corner_radius=5, fg_color="gray", text="Details").grid(row = 0,column = 1,padx = 2)
    ctk.CTkLabel(book, width=90, height=30, corner_radius=5, fg_color="gray", text="Amount").grid(row = 0,column = 2,padx = 2)
    
    def upadate():
        print(0)
        for i,(en,am) in enumerate(a):
            ctk.CTkLabel(book, width=40, height=30, corner_radius=5, text=i+1).grid(row = i+1,column = 0,padx = 2)
            ctk.CTkLabel(book, width=210, height=30, corner_radius=5,  text=en).grid(row =i+1,column = 1,padx = 2)
            ctk.CTkLabel(book, width=90, height=30, corner_radius=5, text=am).grid(row = i+1,column = 2,padx = 2)



# The Main Logic 
    for frame in (add_f, book, remove_F):
        frame.place(x=0, y=0, relwidth=1, relheight=1)




    def show_frame(frame):
        frame.lift()   
    ctk.CTkButton(main,width=106,height=26,text="Add Entery",command=lambda:show_frame(add_f)).pack(padx = 10,pady = 10,side = "bottom")
    ctk.CTkButton(main,width=30,height=30,text="Remove Entery",command=lambda:show_frame(remove_F)).pack(padx = 10,pady = 10,side = "bottom")
    ctk.CTkButton(main,width=106,height=30,text="Show Entery",command=lambda:show_frame(book),).pack(pady = 10,side = "bottom")
    show_frame(add_f)

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

from customtkinter import CTk
import customtkinter as ctk

ctk.set_appearance_mode("system")

if __name__ == "__main__":
    app = ctk.CTk()
# Main Frame  
    main = ctk.CTkFrame(master=app,width=195,height=280)
    main.pack(expand=True, side="left", fill="both",padx = 5,pady = 5) 
    content_frame = ctk.CTkFrame(master=app,width=395,height=330)
    content_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)
# For Adding The Entery 
    add_f = ctk.CTkFrame(master=content_frame)
    # add_f.pack(expand = False,side = "right",fill = "both",padx = 5,pady=5)
    entery = ctk.CTkEntry(add_f,placeholder_text="Enter The Entery",width=70,height=30)
    entery.place(x = 100,y = 200,)
    
# For removing The Entery
    remove_F = ctk.CTkFrame(master=content_frame)
    


# For Viwe All Entery
    book = ctk.CTkScrollableFrame(master=content_frame,)




# The Main Logic 
    for frame in (add_f, book, remove_F):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    def show_frame(frame):
        frame.lift()   
    ctk.CTkButton(main,width=106,height=30,text="Add Entery",command=lambda:show_frame(add_f)).pack(padx = 10,pady = 10,side = "bottom")
    ctk.CTkButton(main,width=30,height=30,text="REMOVE Entery",command=lambda:show_frame(remove_F)).pack(padx = 10,pady = 10,side = "bottom")
    ctk.CTkButton(main,width=106,height=30,text="Show Entery",command=lambda:show_frame(book)).pack(pady = 10,side = "bottom")
    mess = ctk.CTkLabel(master=main,text="Welcome To Money Management \n App",width=185,height=185)
    mess.pack(side = "top",padx = 10,pady = 5)






    show_frame(add_f)


    app.geometry("600x350")
    app.resizable(False,False)
    app.mainloop()

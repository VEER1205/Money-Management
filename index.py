from customtkinter import CTk
import customtkinter as ctk

ctk.set_appearance_mode("system")

if __name__ == "__main__":
    app = ctk.CTk()
    main = ctk.CTkFrame(master=app,width=195,height=280)
    main.pack(expand=True, side="left", fill="both",padx = 5,pady = 5) 
    content_frame = ctk.CTkFrame(master=app,width=395,height=330)
    content_frame.pack(side="right", expand=True, fill="both", padx=5, pady=5)
# For Adding The Entery 
    add_f = ctk.CTkFrame(master=content_frame)
    # add_f.pack(expand = False,side = "right",fill = "both",padx = 5,pady=5)
    in_text = ctk.CTkEntry(master=add_f,width = 280,height= 30,placeholder_text="ENTER NOTE")
    in_text.grid(row=0, column=0, padx=1, pady=1)
    re_text = ctk.CTkEntry(master=add_f,width= 80,height=30,placeholder_text="AMOUNT")
    re_text.grid(row = 0,column = 1,padx =3)
# For removing The Entery
    remove_F = ctk.CTkFrame(master=content_frame)

# For Viwe All Entery
    book = ctk.CTkScrollableFrame(master=content_frame,)



# The Main Logic 
    for frame in (add_f, book, remove_F):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    def show_frame(frame):
        frame.lift()   
    

    show_frame(add_f)


    app.geometry("600x350")
    app.resizable(False,False)
    app.mainloop()

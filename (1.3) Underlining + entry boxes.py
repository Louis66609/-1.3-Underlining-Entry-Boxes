import customtkinter as ctk
import tkinter
import customtkinter
from PIL import ImageTk,Image
import re

def create_window(title):
    ctk.set_default_color_theme("green")
    window = ctk.CTk()
    window.geometry("1400x800")
    ctk.set_appearance_mode("light")
    window.resizable(width=False, height=False)
    center_window(window)
    frame = create_frame(window)
    window.wm_title(title)
    return window, frame 

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 1400
    window_height = 800
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def create_frame(window):
    frame = ctk.CTkFrame(master=window, width=750, height=600)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return frame

def login_page():
    Login_page_window, frame = create_window("Login Page")
 
    LogPg_ad_txt = ctk.CTkLabel(master=frame, text="Login as Admin:", font=('Roboto', 25))
    LogPg_ad_txt.place(x=85,y=45)

    LogPg_emp_txt = ctk.CTkLabel(master=frame, text="Login as Employee:", font=('Roboto', 25))
    LogPg_emp_txt.place(x=450,y=45)

    LogPg_accreg1_txt = ctk.CTkLabel(master=frame, font=('Roboto', 18), text="Don't have an account? Register here as an")
    LogPg_accreg1_txt.place(x=15,y=565)
    
    LogPg_accreg2_txt = ctk.CTkLabel(master=frame, text="Or an", font=('Roboto', 18))
    LogPg_accreg2_txt.place(x=490,y=565)

    LogPg_ad_underline = ctk.CTkButton(master=frame, width=190, height=3, corner_radius=0, text="")
    LogPg_ad_underline.place(x=78,y=75)
 
    LogPg_emp_underline = ctk.CTkButton(master=frame, width=230, height=3, corner_radius=0, text="")
    LogPg_emp_underline.place(x=442,y=75)

    LogPG_ad_compnam_entry = ctk.CTkEntry(master=frame, width=260,justify="center",font=('Roboto', 15),placeholder_text='Enter Company Name...')
    LogPG_ad_compnam_entry.place(x=43,y=140)

    LogPG_ad_pass_entry = ctk.CTkEntry(master=frame, width=260, show="*", justify="center",font=('Roboto', 15), placeholder_text='Enter Password...' )
    LogPG_ad_pass_entry.place(x=43,y=240)

    LogPg_emp_username_entry = ctk.CTkEntry(master=frame, width=260, justify="center",font=('Roboto', 15), placeholder_text='Enter Username...')
    LogPg_emp_username_entry.place(x=428,y=140)

    LogPg_emp_pass_entry = ctk.CTkEntry(master=frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPg_emp_pass_entry.place(x=428,y=240)
    
    Login_page_window.mainloop()

login_page()

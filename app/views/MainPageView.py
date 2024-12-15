# views/MainPageView.py
import customtkinter as ctk
from tkinter import *
import os
from PIL import Image, ImageTk

class MainPageView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sidebar(self)
        self.mainpage()

    def sidebar(self,MainParent):
        SidebarParent = ctk.CTkLabel(MainParent,bg_color='#222222',text='')
        SidebarParent.place(anchor="nw", relwidth=0.08, relheight=1)

    def mainpage(self):
        app_logo_path = os.path.join(self.base_dir,"AppLogo.png")
        logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(600,250))
        logo_placeholder = ctk.CTkButton(self,image=logo,fg_color='transparent',text='',state="diabled" ,border_width=0,border_color="white")
        logo_placeholder.place(x=30 , y=240)

        

       

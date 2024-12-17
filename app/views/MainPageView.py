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
        self.main_label = ctk.CTkLabel(self,bg_color='gray20',text='')
        self.main_label.place(anchor="nw", relwidth=1, relheight=1)
        self.sidebar(self)
        self.bottombar(self)
        self.right_section(self)
        self.menu_section(self)

    def sidebar(self,MainParent):
        SidebarParent = ctk.CTkLabel(MainParent,bg_color='white',text='')
        SidebarParent.place(anchor="nw", relwidth=1, relheight=0.1)

        app_logo_path = os.path.join(self.base_dir,"assets","image","AppLogo.png")
        logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(250,60))
        logo_placeholder = ctk.CTkLabel(SidebarParent,image=logo,text='',fg_color='transparent')
        logo_placeholder.place(x=90,y=8)

    def right_section(self,MainParent):
        right_section_Main = ctk.CTkLabel(MainParent,bg_color='grey30',text='', height=637,width=500)
        right_section_Main.place(x=900,y=79)

    def menu_section(self, MainParent):
        MenuSectionMain = ctk.CTkLabel(MainParent,bg_color='white',text='',height=600,width=860)
        MenuSectionMain.place(x=20,y=100)
        
        button_1 = ctk.CTkButton(MenuSectionMain,width=200,height=300,corner_radius=0,fg_color='#5e4c83')
        button_1.place(x=0,y=0)

        button_2 = ctk.CTkButton(MenuSectionMain,width=300,height=300,corner_radius=0)
        button_2.place(x=0,y=300)

        button_3 = ctk.CTkButton(MenuSectionMain,width=200,height=300,corner_radius=0,fg_color='#6798b0')
        button_3.place(x=660,y=0)

        button_4 = ctk.CTkButton(MenuSectionMain,width=460,height=300,corner_radius=0,fg_color='#f09f9c')
        button_4.place(x=200,y=0)

        button_5 = ctk.CTkButton(MenuSectionMain,width=300,height=300,corner_radius=0)
        button_5.place(x=560,y=300)

        app_logo_path = os.path.join(self.base_dir,"assets","image","Applogo2.png")
        logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(180,180))
        logo_placeholder = ctk.CTkLabel(MenuSectionMain,image=logo,text='',fg_color='white')
        logo_placeholder.place(x=340,y=370)

        



    def bottombar(self,MainParent):
        BottombarParent = ctk.CTkLabel(MainParent,bg_color='grey10',text='')
        BottombarParent.place(anchor="sw", relwidth=1, relheight=0.09, rely=1)

    def main_button(self):
        main_button_place = ctk.CTkLabel(self.main_label,bg_color='red',text='') 
        main_button_place.place(x=10,y=200)

        

       

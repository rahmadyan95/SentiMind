import customtkinter as ctk
from tkinter import *
from PIL import Image
import os

class SentimentAnalysisDataListView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sidebar(self)
        self.main_box()
        self.downBox()

    def sidebar(self,MainParent):
        SidebarParent = ctk.CTkLabel(MainParent,bg_color='white',text='')
        SidebarParent.place(anchor="nw", relwidth=1, relheight=0.1)

        HomeLogoPath = os.path.join(self.base_dir,"assets","image","home.png")

        # app_logo_path = os.path.join(self.base_dir,"assets","image","AppLogo.png")
        # logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(250,60))
        # logo_placeholder = ctk.CTkLabel(SidebarParent,image=logo,text='',fg_color='transparent')
        # logo_placeholder.place(x=90,y=8)

        title = ctk.CTkLabel(SidebarParent,text='Choose Data To Analyze',font=('Coda Pro',32),text_color='black',fg_color='white')
        title.place(x=90,y=20)

        HomeLogo = ctk.CTkImage(light_image=Image.open(HomeLogoPath), size=(40,40))
        logo_placeholder = ctk.CTkButton(SidebarParent,image=HomeLogo,text='',fg_color='white',bg_color='white',height=75,width=75,
                                         border_width=2,border_color='grey20',corner_radius=0,command=lambda: self.controller.show_frame("MainPageView"))
        logo_placeholder.place(x=1270,y=2)

    def main_box(self):
        self.scrollbox = ctk.CTkScrollableFrame(self,height=570,width=1300,fg_color='grey30')
        self.scrollbox.place(x=15,y=100)

    def downBox(self):
        self.dropBox = ctk.CTkButton(self, height=80,width=1320,fg_color='grey30',corner_radius=6,state='disabled')
        self.dropBox.place(x=15,y=695)
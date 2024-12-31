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
        self.ColoumnBar()

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

    def ColoumnBar(self):
        ColoumnBarMainBox = ctk.CTkButton(self,height=70,width=1350,text='',bg_color='transparent',corner_radius=5,fg_color='grey30',state='disabled')
        ColoumnBarMainBox.place(x=15,y=90)

        NumberLabel = ctk.CTkLabel(ColoumnBarMainBox,text='NO.',font=('Coda Pro',24),text_color='white',bg_color='transparent',fg_color='transparent')
        NumberLabel.place(x=35,y=20)

        ProductLabel = ctk.CTkLabel(ColoumnBarMainBox,text='Name File',font=('Coda Pro',24),text_color='white',bg_color='transparent',fg_color='transparent')
        ProductLabel.place(x=150,y=20)

        LastUpdateLabel = ctk.CTkLabel(ColoumnBarMainBox,text='Last Update',font=('Coda Pro',24),text_color='white',bg_color='transparent',fg_color='transparent')
        LastUpdateLabel.place(x=300,y=20)




    def main_box(self):

        trashcaniconpath = os.path.join(self.base_dir,"assets","image","trashcanicon.png")
        refreshiconpath = os.path.join(self.base_dir,"assets","image","refreshicon.png")

        trashcanicon = ctk.CTkImage(light_image=Image.open(trashcaniconpath), size=(50,50))
        refreshicon = ctk.CTkImage(light_image=Image.open(refreshiconpath), size=(50,50))

        self.scrollbox = ctk.CTkScrollableFrame(self,height=510,width=1300,fg_color='grey30')
        self.scrollbox.place(x=15,y=170)

        for i in range(4):

            NumberBox = ctk.CTkButton(self.scrollbox,height=80,width=80,text=f'{i}',bg_color='transparent',corner_radius=5,fg_color='grey20',state='disabled')
            NumberBox.grid(row=i, column=0,padx=10, pady=5)

            DataMainBox = ctk.CTkButton(self.scrollbox,height=80,width=810,text='',bg_color='transparent',corner_radius=5,fg_color='grey20',state='disabled')
            DataMainBox.grid(row=i, column=1,padx=5, pady=5)

            self.deleteButton = ctk.CTkButton(self.scrollbox,height=80,width=80,text='',image=trashcanicon,bg_color='transparent',corner_radius=5,fg_color='#E54C38',hover_color='#C23A22')
            self.deleteButton.grid(row=i, column=2,padx=5, pady=5)
            
            self.refreshButton = ctk.CTkButton(self.scrollbox,height=80,width=80,bg_color='transparent',text='',image=refreshicon,corner_radius=5,fg_color='#80ef80',hover_color='#8cbd8c')
            self.refreshButton.grid(row=i, column=3,padx=5, pady=5)

            self.StartAnalyzeButton = ctk.CTkButton(self.scrollbox,height=80,width=180,bg_color='transparent',corner_radius=5,fg_color='grey20')
            self.StartAnalyzeButton.grid(row=i, column=4,padx=5, pady=5)

            
    


    def downBox(self):
        self.dropBox = ctk.CTkButton(self, height=80,width=1320,fg_color='grey30',corner_radius=6,state='disabled')
        self.dropBox.place(x=15,y=694)

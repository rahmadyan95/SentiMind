import customtkinter as ctk
from tkinter import *
from PIL import Image
import os
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.controllers.TokopediaScrapperController import TokopediaScrapperController

class SentimentAnalysisDataListView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.controllerInstances = TokopediaScrapperController()
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
        ColoumnBarMainBox = ctk.CTkButton(self,height=70,width=1320,text='',bg_color='transparent',corner_radius=5,fg_color='grey30',state='disabled')
        ColoumnBarMainBox.place(x=15,y=90)

        NumberLabel = ctk.CTkLabel(ColoumnBarMainBox,text='NO.',font=('Coda Pro',20),text_color='white',bg_color='transparent',fg_color='transparent')
        NumberLabel.place(x=35,y=20)

        IdLabel = ctk.CTkLabel(ColoumnBarMainBox,text='Scrap ID',font=('Coda Pro',20),text_color='white',bg_color='transparent',fg_color='transparent')
        IdLabel.place(x=130,y=20)

        Platform = ctk.CTkLabel(ColoumnBarMainBox,text='Platform',font=('Coda Pro',20),text_color='white',bg_color='transparent',fg_color='transparent')
        Platform.place(x=280,y=20)

        date = ctk.CTkLabel(ColoumnBarMainBox,text='Date',font=('Coda Pro',20),text_color='white',bg_color='transparent',fg_color='transparent')
        date.place(x=470,y=20)

        title = ctk.CTkLabel(ColoumnBarMainBox,text='Video / Product Title',font=('Coda Pro',20),text_color='white',bg_color='transparent',fg_color='transparent')
        title.place(x=780,y=20)


    def main_box(self):

        GetAllScrappingData = self.controllerInstances.GetAllScrappingData()
        print(GetAllScrappingData)

        trashcaniconpath = os.path.join(self.base_dir,"assets","image","trashcanicon.png")
        refreshiconpath = os.path.join(self.base_dir,"assets","image","refreshicon.png")

        trashcanicon = ctk.CTkImage(light_image=Image.open(trashcaniconpath), size=(50,50))
        refreshicon = ctk.CTkImage(light_image=Image.open(refreshiconpath), size=(50,50))

        self.scrollbox = ctk.CTkScrollableFrame(self,height=510,width=1300,fg_color='grey30')
        self.scrollbox.place(x=15,y=170)

        for i,row in enumerate(GetAllScrappingData):
            
            platform,scrapID,title,date = row

            NumberBox = ctk.CTkLabel(self.scrollbox,height=70,width=70,text=f'{i}',font=('Coda Pro',20),bg_color='transparent',corner_radius=0,fg_color='grey20',state='disabled')
            NumberBox.grid(row=i, column=0,padx=5, pady=5)

            scrapIDPlaceholder = ctk.CTkLabel(self.scrollbox,height=70,width=150,text=f'{scrapID}',font=('Coda Pro',14),bg_color='transparent',corner_radius=0,fg_color='grey20',state='disabled')
            scrapIDPlaceholder.grid(row=i, column=1,padx=5, pady=5)

            platformPlaceholder = ctk.CTkLabel(self.scrollbox,height=70,width=150,text=f'{platform}',font=('Coda Pro',14),bg_color='transparent',corner_radius=0,fg_color='grey20',state='disabled')
            platformPlaceholder.grid(row=i, column=2,padx=5, pady=5)

            datePlaceholder = ctk.CTkLabel(self.scrollbox,height=70,width=170,text=f'{date}',font=('Coda Pro',14),bg_color='transparent',corner_radius=0,fg_color='grey20',state='disabled')
            datePlaceholder.grid(row=i, column=3,padx=5, pady=5)

            titlePlaceholder = ctk.CTkLabel(self.scrollbox,height=70,width=550,text=f'',font=('Coda Pro',14),anchor='w',bg_color='transparent',corner_radius=0,fg_color='grey20',state='disabled',wraplength=500)
            titlePlaceholder.grid(row=i, column=4,padx=5, pady=5)

            titlePlaceholderChild = ctk.CTkLabel(titlePlaceholder,text=f'{title}',font=('Coda Pro',14),anchor='w',bg_color='transparent',corner_radius=0,fg_color='grey20',state='disabled',wraplength=535)
            titlePlaceholderChild.place(x=15,y=15)
            

            

            # self.deleteButton = ctk.CTkButton(self.scrollbox,height=70,width=70,text='',image=trashcanicon,bg_color='transparent',corner_radius=0,fg_color='#E54C38',hover_color='#C23A22')
            # self.deleteButton.grid(row=i, column=2,padx=5, pady=5)
            
            # self.refreshButton = ctk.CTkButton(self.scrollbox,height=70,width=70,bg_color='transparent',text='',image=refreshicon,corner_radius=0,fg_color='#70ef70',hover_color='#8cbd8c')
            # self.refreshButton.grid(row=i, column=3,padx=5, pady=5)

            self.StartAnalyzeButton = ctk.CTkButton(self.scrollbox,height=70,width=150,bg_color='transparent',corner_radius=0,fg_color='grey20',
                                                    command=lambda vid=scrapID: self.analyze(vid))
            self.StartAnalyzeButton.grid(row=i, column=5,padx=5, pady=5)

            
    
    def analyze(self, video_id):
        """
        Fungsi ini akan dipanggil saat tombol Start Analyze ditekan.
        """
        print(f"Analyzing Video ID: {video_id}")

    def downBox(self):
        self.dropBox = ctk.CTkButton(self, height=75,width=1320,fg_color='grey30',corner_radius=4,state='disabled')
        self.dropBox.place(x=15,y=702)

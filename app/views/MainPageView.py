# views/MainPageView.py
import customtkinter as ctk
from tkinter import *
import os
from PIL import Image, ImageTk



# MainFont = ctk.CTkFont()


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

        box_1 = ctk.CTkLabel(right_section_Main,text='',height=300,width=400, bg_color="grey20")
        box_1.place(x=28,y=20)

        box_1_title = ctk.CTkLabel(right_section_Main,text='Total Comments Dataset',
                                   text_color="black",height=65,width=415, 
                                   bg_color="#B3C8CF",font=('Coda Pro',20))
        box_1_title.place(x=20,y=20)



    def menu_section(self, MainParent):

        MenuSectionMain = ctk.CTkLabel(MainParent,bg_color='white',text='',height=600,width=860)
        MenuSectionMain.place(x=20,y=100)

        # ============================== SECTION PATH ===========================================
        TokopediaLogoPath = os.path.join(self.base_dir,"assets","image","logo-tokopedia.png")
        ShopeeLogoPath = os.path.join(self.base_dir,"assets","image","shopee-logo2.png")
        YoutubeLogoPath = os.path.join(self.base_dir,"assets","image","Youtube-Logo.png")
        DBLogoPath = os.path.join(self.base_dir,"assets","image","db_logo.png")
        SentimentAnalysisLogoPath = os.path.join(self.base_dir,"assets","image","sentiment_analysis.png")


        
        # =============================== END SECTION PATH ======================================

        app_logo_path = os.path.join(self.base_dir,"assets","image","Applogo2.png")
        logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(180,180))
        logo_placeholder = ctk.CTkLabel(MenuSectionMain,image=logo,text='',fg_color='white')
        logo_placeholder.place(x=340,y=370)


        # TOKOPEDIA SCRAPPER BUTTON ======== START ========
        TokopediaLogo = ctk.CTkImage(light_image=Image.open(TokopediaLogoPath), size=(165,60))
        TokopediaScrapperButton = ctk.CTkButton(MenuSectionMain,width=200,height=300,corner_radius=0,fg_color='#A5E1A6',text='',
                                 font=('Coda Pro',28),image=TokopediaLogo,hover_color='grey30')
        TokopediaScrapperButton.place(x=0,y=0)
        
        # TokopediaLogoPlaceholder = ctk.CTkButton(TokopediaScrapperButton,image=TokopediaLogo,text='')
        # TokopediaLogoPlaceholder.place(x=20,y=20)

        # TOKOPEDIA SCRAPPER BUTTON ======== END ========

        # SHOPEE SCRAPPER BUTTON ======== START  ========
        ShopeeLogo = ctk.CTkImage(light_image=Image.open(ShopeeLogoPath), size=(200,85))
        ShopeeScrapperPageButton = ctk.CTkButton(MenuSectionMain,image=ShopeeLogo,text='',width=300,height=300,corner_radius=0,hover_color='grey30',fg_color='#FFB082')
        ShopeeScrapperPageButton.place(x=0,y=300)

        # SHOPEE SCRAPPER BUTTON ======== END  ========

        
        # YOUTUBE SCRAPPER BUTTON ======== START ========
        YoutubeLogo = ctk.CTkImage(light_image=Image.open(YoutubeLogoPath), size=(165,55))
        YoutubeScrapperPageButton = ctk.CTkButton(MenuSectionMain,width=200,height=300,corner_radius=0,fg_color='white',text='',image=YoutubeLogo,hover_color='grey30',command=lambda: self.controller.show_frame("YoutubeScrapperView"))
        YoutubeScrapperPageButton.place(x=660,y=0)

        # YOUTUBE SCRAPPER BUTTON ======== STOP ========

        # SENTIMENT ANALYSIS BUTTON ========== START ============
        
        SentimentAnalysisLogo = ctk.CTkImage(light_image=Image.open(SentimentAnalysisLogoPath), size=(380,75))
        SentimentAnalysisPageButton = ctk.CTkButton(MenuSectionMain,width=460,height=300,corner_radius=0,fg_color='#f09f9c',
                                 text='',font=('Coda Pro',32),text_color='black',hover_color='grey30',image=SentimentAnalysisLogo)
        SentimentAnalysisPageButton.place(x=200,y=0)

        # SENTIMENT ANALYSIS BUTTON ========== END ============


        # DATABASE BUTTON PAGE  ========== START  ============


        DBLogo = ctk.CTkImage(light_image=Image.open(DBLogoPath), size=(230,75))
        DBPageButton = ctk.CTkButton(MenuSectionMain,width=300,height=300,corner_radius=0,text='',image=DBLogo,fg_color='#B3C8CF',hover_color='grey30')
        DBPageButton.place(x=560,y=300)

        # DATABASE BUTTON PAGE  ========== END  ============

       

        
    def bottombar(self,MainParent):
        BottombarParent = ctk.CTkLabel(MainParent,bg_color='grey10',text='')
        BottombarParent.place(anchor="sw", relwidth=1, relheight=0.09, rely=1)

        # =============== SECTION PATH POWERED BY ==============================
        PoweredByLogoPath  = os.path.join(self.base_dir,"assets","image","Logo.png")
        PoweredByLogo = ctk.CTkImage(light_image=Image.open(PoweredByLogoPath), size=(390,45))

        logo_placeholder = ctk.CTkLabel(BottombarParent,image=PoweredByLogo,text='',bg_color='grey10')
        logo_placeholder.place(x=10,y=15)





    def main_button(self):
        main_button_place = ctk.CTkLabel(self.main_label,bg_color='red',text='') 
        main_button_place.place(x=10,y=200)

        

       

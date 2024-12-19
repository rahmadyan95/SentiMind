import customtkinter as ctk
import os
from PIL import Image
import customtkinter
from CTkTable import *
from pandastable import Table,TableModel
import tkinter as tk



class TokopediaScrapperView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sidebar(self)
        self.right_section(self)
        self.left_side()

        # self.controller.master.bind("<KP_8>", self.handle_arrow_keys)

        

    def sidebar(self,MainParent):
        SidebarParent = ctk.CTkLabel(MainParent,bg_color='white',text='')
        SidebarParent.place(anchor="nw", relwidth=1, relheight=0.1)

        app_logo_path = os.path.join(self.base_dir,"assets","image","AppLogo.png")
        logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(250,60))
        logo_placeholder = ctk.CTkLabel(SidebarParent,image=logo,text='',fg_color='transparent')
        logo_placeholder.place(x=90,y=8)

    def right_section(self,MainParent):
        right_section_Main = ctk.CTkLabel(MainParent,bg_color='grey30',text='', height=750,width=500)
        right_section_Main.place(x=900,y=79)

        box_1 = ctk.CTkLabel(right_section_Main,text='',height=300,width=400, bg_color="grey20")
        box_1.place(x=28,y=20)

        box_1_title = ctk.CTkLabel(right_section_Main,text='Total Comments Dataset',
                                   text_color="black",height=65,width=415, 
                                   bg_color="#B3C8CF",font=('Coda Pro',20))
        box_1_title.place(x=20,y=20)

    def left_side(self):
        link_box = ctk.CTkLabel(self,height=70,width=870,bg_color='grey30',text='')
        link_box.place(x=15,y=100)

        TabelBox = ctk.CTkScrollableFrame(self,height=575,width=850,bg_color='transparent',
                                          fg_color='grey30')
        TabelBox.place(x=15,y=185)

        TablePlaceholder = ctk.CTkLabel(TabelBox)
        TablePlaceholder.grid(padx=0.5,pady=0.5)

        value = [[1,2],
                [1,2],
                [1,2],
                [1,2],
                [1,2]]
        
        table = CTkTable(TablePlaceholder, row=100, column=2, values=value)
        table.grid()

        


        
        


    
    

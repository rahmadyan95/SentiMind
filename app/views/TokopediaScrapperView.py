import customtkinter as ctk
import os
from PIL import Image
import customtkinter
from CTkTable import *
from pandastable import Table,TableModel
import tkinter as tk
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from controllers.TokopediaScrapperController import TokopediaScrapperController



class TokopediaScrapperView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.InstancesControler = TokopediaScrapperController()

        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sidebar(self)
        self.right_section(self)
        self.left_side()
        self.show_table()
        

        # self.controller.master.bind("<KP_8>", self.handle_arrow_keys)

        

    def sidebar(self,MainParent):
        SidebarParent = ctk.CTkLabel(MainParent,bg_color='white',text='')
        SidebarParent.place(anchor="nw", relwidth=1, relheight=0.1)

        app_logo_path = os.path.join(self.base_dir,"assets","image","AppLogo.png")
        logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(250,60))
        logo_placeholder = ctk.CTkLabel(SidebarParent,image=logo,text='',fg_color='transparent')
        logo_placeholder.place(x=90,y=8)

    def right_section(self,MainParent):
        right_section_Main = ctk.CTkLabel(MainParent,bg_color='grey30',text='', height=750,width=500,)
        right_section_Main.place(x=900,y=79)

        box_1 = ctk.CTkButton(right_section_Main,text='',height=250,width=400,bg_color='transparent',fg_color="grey20",state='disabled',corner_radius=4)
        box_1.place(x=28,y=20)

        box_1_title = ctk.CTkLabel(right_section_Main,text='Input Data',
                                   text_color="grey20",height=50,width=415, 
                                   bg_color="#B3C8CF",font=('Coda Pro',20))
        box_1_title.place(x=20,y=20)

        YoutubeLinkTitle = ctk.CTkLabel(box_1, font=('FiraCode Nerd Font',18),text="Youtube Link:")
        YoutubeLinkTitle.place(x=10, y=60)

        YoutubeMaxCommentTitle = ctk.CTkLabel(box_1, font=('FiraCode Nerd Font',14),text="Max. Scrap")
        YoutubeMaxCommentTitle.place(x=300, y=60)

        YoutubeLinkInput = ctk.CTkTextbox(box_1,height=90,width=280,fg_color='grey30',
                                          font=('FiraCode Nerd Font',18),corner_radius=3)
        YoutubeLinkInput.place(x=10,y=90)

        SumOfCommentar = ctk.CTkTextbox(box_1,height=90,width=90,fg_color='grey30',
                                          font=('FiraCode Nerd Font',43),corner_radius=3)
        SumOfCommentar.place(x=300,y=90)

        SearchButton = ctk.CTkButton(box_1,height=40,width=380,fg_color='#6c8ca4',font=('Coda Pro',18),
                                     text='SEARCH',hover_color='grey50',text_color='black',corner_radius=3)
                                     
        SearchButton.place(x=10, y=190)

        self.statistic_box = ctk.CTkScrollableFrame(right_section_Main,height=290,width=380,bg_color='transparent',
                                          fg_color='grey20')
        self.statistic_box.place(x=28,y=330)
        
        box_2_title = ctk.CTkLabel(right_section_Main,text='Cleanned Data Statistic',
                                   text_color="grey20",height=50,width=415, 
                                   bg_color="#B3C8CF",font=('Coda Pro',20))
        box_2_title.place(x=20,y=280)

        submit_button = ctk.CTkButton(right_section_Main,height=40,width=415,fg_color='#5DB996',font=('Coda Pro',18),
                                     text='Save to database 🗂️',hover_color='#118B50',text_color='black',corner_radius=3)
                                     
        submit_button.place(x=20, y=650)

    


    def left_side(self):
        link_box = ctk.CTkLabel(self,height=70,width=870,bg_color='grey30',text='')
        link_box.place(x=15,y=100)

        self.TabelBox = ctk.CTkScrollableFrame(self,height=575,width=850,bg_color='transparent',
                                          fg_color='grey30')
        self.TabelBox.place(x=15,y=185)



    def show_table(self):
        result = self.InstancesControler.get_data("https://www.youtube.com/watch?v=kBQP6A_BmQs", 10)
        cleaned_comments = result['cleaned_comments']
        # table = CTkTable(self.TabelBox,row=value[1], column=1, values=value[0],corner_radius=0,
        #                  font=('Coda Pro',15),width=840,wraplength=1500,justify='W')
        # table.grid(padx=0, pady=0, sticky='nw')
        values = [[comment] for comment in cleaned_comments]
        row_count = len(values)
        
        table = CTkTable(
            self.TabelBox,
            row=row_count,
            column=1,
            values=values,
            corner_radius=0,
            font=('Coda Pro', 15),
            width=840,
            wraplength=1500,
            justify='W'
        )
        table.grid(padx=0, pady=0, sticky='nw')

        datalist = [
            ('Emoji', result['total_emoji_removed']),
            ('Url', result['total_url_removed']),
            ('Character', result['total_char_removed']),
            ('Digit', result['total_digit_removed']),
            ('Whitespace', result['total_whitespace_removed'])
        ]   

        for data, count in datalist:
            CleannedBox = ctk.CTkLabel(self.statistic_box, height=135, width=365, text='', fg_color='grey30',
                                    corner_radius=4)
            CleannedBox.grid(padx=10, pady=5)

            CleannedTitle = ctk.CTkLabel(CleannedBox, text=f'{data} Cleanned Count :', font=('FiraCode Nerd Font', 18),
                                        fg_color='grey30', corner_radius=4)
            CleannedTitle.place(x=10, y=10)

            CleannedText = ctk.CTkLabel(CleannedBox, text=f'{count}', font=('FiraCode Nerd Font', 45),
                                        fg_color='grey30', corner_radius=4)
            CleannedText.place(x=155, y=55)

        

        


        
        


    
    

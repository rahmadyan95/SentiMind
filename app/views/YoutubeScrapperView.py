import customtkinter as ctk
import os
from PIL import Image
import customtkinter
from CTkTable import *
from pandastable import Table,TableModel
import tkinter as tk
import pandas as pd
from CTkMessagebox import CTkMessagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.controllers.YoutubeScrapperController import YoutubeScrapperController
import sqlite3


class YoutubeScrapperView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.InstancesControler = YoutubeScrapperController()

        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sidebar(self)
        self.right_section(self)
        self.left_side()
        # self.show_table()
        

        # self.controller.master.bind("<KP_8>", self.handle_arrow_keys)

        
    def sidebar(self,MainParent):
        SidebarParent = ctk.CTkLabel(MainParent,bg_color='white',text='')
        SidebarParent.place(anchor="nw", relwidth=1, relheight=0.1)

        app_logo_path = os.path.join(self.base_dir,"assets","image","AppLogo.png")
        HomeLogoPath = os.path.join(self.base_dir,"assets","image","home.png")
        
        logo = ctk.CTkImage(light_image=Image.open(app_logo_path), size=(250,60))
        logo_placeholder = ctk.CTkLabel(SidebarParent,image=logo,text='',fg_color='transparent')
        logo_placeholder.place(x=90,y=8)

        HomeLogo = ctk.CTkImage(light_image=Image.open(HomeLogoPath), size=(40,40))
        logo_placeholder = ctk.CTkButton(SidebarParent,image=HomeLogo,text='',fg_color='white',bg_color='white',height=75,width=75,
                                         border_width=2,border_color='grey20',corner_radius=0,command=lambda: self.controller.show_frame("MainPageView"))
        logo_placeholder.place(x=1270,y=2)


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

        self.YoutubeLinkInput = ctk.CTkEntry(box_1,height=90,width=280,fg_color='grey30',
                                          font=('FiraCode Nerd Font',18),corner_radius=3,placeholder_text="Input Youtube Link")
        self.YoutubeLinkInput.place(x=10,y=90)

        self.SumOfCommentar = ctk.CTkEntry(box_1,height=90,width=90,fg_color='grey30',
                                          font=('FiraCode Nerd Font',43),corner_radius=3,
                                          placeholder_text='Max 100')
        self.SumOfCommentar.place(x=300,y=90)

        SearchButton = ctk.CTkButton(box_1,height=40,width=380,fg_color='#6c8ca4',font=('Coda Pro',18),
                                     text='SEARCH',hover_color='grey50',text_color='black',corner_radius=3,
                                     command=self.validate)
                                     
        SearchButton.place(x=10, y=190)

        self.statistic_box = ctk.CTkScrollableFrame(right_section_Main,height=290,width=380,bg_color='transparent',
                                          fg_color='grey20')
        self.statistic_box.place(x=28,y=330)
        
        box_2_title = ctk.CTkLabel(right_section_Main,text='Cleanned Data Statistic',
                                   text_color="grey20",height=50,width=415, 
                                   bg_color="#B3C8CF",font=('Coda Pro',20))
        box_2_title.place(x=20,y=280)

        submit_button = ctk.CTkButton(right_section_Main,height=40,width=300,fg_color='#5DB996',font=('Coda Pro',18),
                                     text='Save to database 🗂️',hover_color='#118B50',text_color='black',corner_radius=3,
                                     command=self.SaveToDatabase)
                                     
        submit_button.place(x=130, y=650)

        reload_button = ctk.CTkButton(right_section_Main,height=40,width=100,fg_color='#5DB996',font=('Coda Pro',18),
                                     text='Reload ⟳',hover_color='#FCDC94',text_color='black',corner_radius=3,command=self.reload_data)
                                     
        reload_button.place(x=25, y=650)

    def validate(self):
        if not self.YoutubeLinkInput.get() or not self.SumOfCommentar.get():
            msg = CTkMessagebox(self,title="Warning", message="Youtube Link or Max of commentar is empty",
                        icon="warning", option_1="Return")
            response = msg.get()
            
            if response=="Return":
                return
            
        else :
            self.show_table()


    def left_side(self):
        link_box = ctk.CTkLabel(self,height=70,width=870,bg_color='grey30',text='')
        link_box.place(x=15,y=100)

        self.LinkPlaceholder = ctk.CTkLabel(link_box, font=('FiraCode Nerd Font',18),text="Video Title :",bg_color='grey30')
        self.LinkPlaceholder.place(x=15, y=20)

        self.link_input = ctk.CTkLabel(link_box, font=('FiraCode Nerd Font',18),text="",fg_color='grey20',height=45,width=680)
        self.link_input.place(x=180, y=12)

        self.link_place = ctk.CTkLabel(self.link_input, font=('FiraCode Nerd Font',15),text=f"")
        self.link_place.place(x=10, y=10)
        

        self.TabelBox = ctk.CTkScrollableFrame(self,height=575,width=850,bg_color='transparent',
                                          fg_color='grey30')
        self.TabelBox.place(x=15,y=185)

    

    def show_table(self):
        num_of_commnet : int = self.SumOfCommentar.get()
        self.result = self.InstancesControler.get_data(self.YoutubeLinkInput.get(), num_of_commnet)
        
        self.title = self.result['video_title']
        cleaned_comments = self.result['comments_data']
        values = [[comment] for comment in cleaned_comments]
        row_count = len(values)

        self.link_place.configure(text=f"{self.title}")


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
            ('Emoji', self.result['total_emoji_removed']),
            ('Url', self.result['total_url_removed']),
            ('Character', self.result['total_char_removed']),
            ('Digit', self.result['total_digit_removed']),
            ('Whitespace', self.result['total_whitespace_removed'])
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
            CleannedText.place(relx=0.5, rely=0.6, anchor="center")

    def SaveToDatabase(self):
        print(self.result)  # For debugging purposes, to check the content of self.result
        try:
            # Ensure self.result contains the correct data (e.g., video_data)
            if not self.result:
                raise ValueError("No data to save.")
            
            self.InstancesControler.SaveToDatabase(self.result)

        except ValueError as ve:
            print(f"Data error: {ve}")
        except sqlite3.Error as db_error:
            print(f"Database error: {db_error}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def reload_data(self):
        # Clear the table and statistics
        for widget in self.link_input.winfo_children():
            widget.destroy()

        for widget in self.TabelBox.winfo_children():
            widget.destroy()

        for widget in self.statistic_box.winfo_children():
            widget.destroy()

        self.YoutubeLinkInput.delete(0, tk.END)
        self.SumOfCommentar.delete(0, tk.END)

        # Recreate the link_place label
        self.link_place = ctk.CTkLabel(self.link_input, font=('FiraCode Nerd Font', 15), text="")
        self.link_place.place(x=10, y=10)

        ctk.CTkLabel(self, text="Data reloaded successfully!", font=('Coda Pro', 18)).place(x=400, y=800)


        

        


        
        


    
    

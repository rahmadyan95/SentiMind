import os
import sys
import sqlite3
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from models.TokopediaScrapperModel import TokopediaScrapperModel
from utils.utils import utils
from app.database.database import DatabaseUtils

class TokopediaScrapperController:
    def __init__(self):
        self.scrapperInstances = TokopediaScrapperModel()
        self.utilsInstances = utils()
        self.DB = DatabaseUtils()

    
    def start_scrapping(self,url,page):
        # if self.utilsInstances.connection_check() == True :
        #     try :
        #         return self.scrapperInstances.start_scrapping(url,page)
        #     except Exception as e:
        #         return e
            
        # else : 
        #     return "Check Your Internet Connection"

        return self.scrapperInstances.start_scrapping(url,page)
    
    def SaveToDatabase(self, video_data):
        """
        Saves the provided video data to the database.

        Args:
            video_data (dict): Dictionary containing video details and comments data.
        """

        try:
            # Attempt to save the video data
            saved_data = self.DB.save_to_database(video_data)
            if saved_data:
                print("Data saved successfully")
            else:
                print("Failed to save data.")
        except sqlite3.Error as e:
            # Handle SQLite-specific errors
            print(f"SQLite error occurred: {e}")
            return False
        except Exception as e:
            # Catch any other exceptions
            print(f"Error to save: {e}")
            return False



    def GetAllScrappingData(self):
        return self.DB.GetData()
            



import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.models.YoutubeScrapperModel import YoutubeScrapperModel
from app.database.database import DatabaseUtils
import sqlite3

class TokopediaScrapperController:
    def get_data(self,youtube_link,num_commets):
        instance = YoutubeScrapperModel()
        return instance.get_comments(youtube_link=youtube_link,max_comments=num_commets)
    
    def validate_input(self,text_a,text_b):
        if not text_a and not text_b :
            return False
        else : 
            True
    
    def SaveToDatabase(self, video_data):
        """
        Saves the provided video data to the database.

        Args:
            video_data (dict): Dictionary containing video details and comments data.
        """
        DB = DatabaseUtils()
        try:
            # Attempt to save the video data
            saved_data = DB.save_to_database(video_data)
            if saved_data:
                print("Data saved successfully")
            else:
                print("Failed to save data.")
        except sqlite3.Error as e:
            # Handle SQLite-specific errors
            print(f"SQLite error occurred: {e}")
        except Exception as e:
            # Catch any other exceptions
            print(f"Error to save: {e}")

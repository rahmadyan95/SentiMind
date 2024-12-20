import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.models.YoutubeScrapperModel import YoutubeScrapperModel


class TokopediaScrapperController:
    def get_data(self,youtube_link,num_commets):
        instance = YoutubeScrapperModel()
        return instance.get_comments(youtube_link=youtube_link,max_comments=num_commets)
    
    def validate_input(self,text_a,text_b):
        if not text_a and not text_b :
            return False
        else : 
            True
    
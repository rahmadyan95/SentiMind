import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.models.YoutubeScrapperModel import YoutubeScrapperModel


class TokopediaScrapperController:
    def get_data(self,youtube_link,num_commets):
        # Create an instance of TokopediaScrapperModels
        instance = YoutubeScrapperModel()
        return instance.get_comments(youtube_link=youtube_link,max_comments=num_commets)

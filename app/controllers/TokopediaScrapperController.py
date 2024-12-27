import os
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from models.TokopediaScrapperModel import TokopediaScrapperModel
from utils.utils import utils

class TokopediaScrapperController:
    def __init__(self):
        self.scrapperInstances = TokopediaScrapperModel()
        self.utilsInstances = utils()

    
    def start_scrapping(self,url,page):
        # if self.utilsInstances.connection_check() == True :
        #     try :
        #         return self.scrapperInstances.start_scrapping(url,page)
        #     except Exception as e:
        #         return e
            
        # else : 
        #     return "Check Your Internet Connection"

        return self.scrapperInstances.start_scrapping(url,page)
            



import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.database.database import DatabaseUtils

class DatabaseController:
    def __init__(self):
        self.DB  = DatabaseUtils()

    def GetAllDataByScrapID(self,ID):
        return self.DB.fetch_data_by_scrapID(ID)
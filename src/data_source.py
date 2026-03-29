"""
DataSource
-----------
"""

#   import pandas library for its csv tools
import pandas as pd
#   import Path from pathlib in order to store the filepath of the csv file
from pathlib import Path

class DataSource (object):
    def __init__(self, name:str, path:Path, format:str):
        self.name = name
        self.path = path
        self.format = format

    def load(self):
        return pd.read_csv(self.path, encoding='latin1')
    
#source = DataSource("polls", Path("/workspaces/comp09049-studyproject-holyrood-forecast-prototype/data/processed/polling_data_processed(Sheet2).csv"), "csv")
"""
DataSource
-----------

The DataSource class allows the name of a data source to be stored along with 
its path and format.

This class also includes a method that enables the csv file to be read and loaded into
the script

"""

#   import pandas library for its csv tools
import pandas as pd
#   import Path from pathlib in order to store the filepath of the csv file
from pathlib import Path

class DataSource (object):
    def __init__(self, name:str, path:Path, format:str):
        self.name = name    #   name of the data source
        self.path = path    #   path where the file is located
        self.format = format    #   file format

    def load(self):
        #   returns the contents of the file
        return pd.read_csv(self.path, encoding='latin1')    #   encoding used to prevent a python crash, original file is an Excel file using latin1 encoding
    
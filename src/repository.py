"""
FileRepository
--------------
"""

from pathlib import Path
import pandas as pd

class FileRepository(object):
    def __init__(self, data_root: Path, outputs_root: Path):
        self.data_root = data_root
        self.outputs_root = outputs_root
    
    def load(self, source):
        return source.load()
    
    def save_results(self, exp_id: str, results):
        path = self.outputs_root/ f"{exp_id}_results.csv"
        pd.DataFrame([results.allocation]).to_csv(path, index=False)
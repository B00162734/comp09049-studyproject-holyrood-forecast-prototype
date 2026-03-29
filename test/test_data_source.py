"""
Unit test for data_source
-------------------------
"""

#   import the class from data_source.py in the src folder
from src.data_source import DataSource

from pathlib import Path
import pandas as pd

source = DataSource("polls", Path("/workspaces/comp09049-studyproject-holyrood-forecast-prototype/data/processed/polling_data_processed(Sheet2).csv"), "csv")

def test_data_source_attributes():

    assert source.name == "polls"
    assert source.format == "csv"
    assert source.path == Path("/workspaces/comp09049-studyproject-holyrood-forecast-prototype/data/processed/polling_data_processed(Sheet2).csv")

def test_data_source_load():
    test_poll = source.load()
    assert isinstance(test_poll, pd.DataFrame)
    assert len(test_poll) > 0

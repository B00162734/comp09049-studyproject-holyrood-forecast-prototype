"""
HolyroodForecastPrototype
-------------------------
"""
from experiment import ForecastExperiment
from datetime import datetime as dt
from config import ForecastConfig
from data_source import DataSource
from pathlib import Path

class HolyroodForecastPrototype(object):
    def main(self):
        t = dt.today()
        tf = t.strftime("%d_%m_%Y_%H:%M")
        exp_no = f"exp_{tf}"

        config = ForecastConfig("baseline", {})
        sources = [DataSource("polls", Path("/workspaces/comp09049-studyproject-holyrood-forecast-prototype/data/processed/polling_data_processed(Sheet2).csv"), "csv")]

                    
        experiment = ForecastExperiment(exp_no, config, sources)
        
        experiment.run()


if __name__ == "__main__":
    HolyroodForecastPrototype().main()
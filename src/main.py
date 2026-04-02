"""
HolyroodForecastPrototype
-------------------------

The HolyroodForecastPrototype class is the main class which calls the experiment class
with the required config and sources data. The file name is formatted with the time 
and date and a message is printed to the terminal to indicate where the output has
been stored.
"""
from experiment import ForecastExperiment
from datetime import datetime as dt
from config import ForecastConfig
from data_source import DataSource
from pathlib import Path

class HolyroodForecastPrototype(object):
    def main(self):
        t = dt.today()  #   fetches the day/date
        tf = t.strftime("%d_%m_%Y_%H:%M")   #   formats the day/date to day_month_year_hours:mins
        exp_no = f"exp_{tf}"    #   stores the formatted day/date in a variable

        config = ForecastConfig("baseline", {}) #   passes in config values
        sources = [DataSource("polls", Path("data/processed/polling_data_processed(Sheet2).csv"), "csv")]    #   passes in sources values

                    
        experiment = ForecastExperiment(exp_no, config, sources)

        experiment.run()

        print("Results have been saved to the output folder")


if __name__ == "__main__":
    HolyroodForecastPrototype().main()
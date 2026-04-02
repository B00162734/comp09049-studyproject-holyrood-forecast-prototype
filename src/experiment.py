"""
ForecastExperiment
-----------------
"""
from data_source import DataSource
from engine import ForecastEngine
from pathlib import Path
from config import ForecastConfig
from allocator import SeatAllocator
from results import ExperimentResults
from repository import FileRepository

class ForecastExperiment(object):
    def __init__(self, id:str, config, sources):
        self.id = id
        self.config = config
        self.sources = sources
    
    def run(self):
    #   for each data source load source data and apply normalisation and weights
        
        for source in self.sources:
            data = source.load()

    #   call generate(data, cfg)
              
            forecast = ForecastEngine().generate(data, self.config)

    #   use returned forecasts to call the seat allocator - allocate_dhondt(forecast)

            allocation = SeatAllocator().allocate_dhondt(forecast.to_dict(),7)

    #   call experiment results  - create(forecast, allocation)
            metrics = 0.05
            results = ExperimentResults(forecast,allocation, metrics)

    #   call file repository to save the results
        outputs_root = Path("outputs")
        data_root = Path("data/processed")
        saved_results  = FileRepository(data_root, outputs_root)
        saved_results.save_results(self.id,results)
        return results

    #   export the saved results to the export reporter - export(exp_id,results,out_dir)


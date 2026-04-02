"""
ForecastConfig
--------------

The ForecastConfig class holds the data which determines the type of model used and a dictionary that stores the bounds for the model parameters

"""

class ForecastConfig(object):
    def __init__(self, name:str, model_params:dict):
        self.name = name    #   name of the model "baseline" or "ML"
        self.model_params = model_params    #   model parameters ensuring the model is bounded
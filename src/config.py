"""
ForecastConfig
--------------

"""

class ForecastConfig(object):
    def __init__(self, name:str, model_params:dict):
        self.name = name
        self.model_params = model_params

config = ForecastConfig("baseline", {"n_polls":5})
print(config.name)
print(config.model_params)

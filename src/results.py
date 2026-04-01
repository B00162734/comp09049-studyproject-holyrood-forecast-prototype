"""
ExperimentResults
-------
"""

class ExperimentResults(object):
    def __init__(self, forecast, allocation, metrics):
        self.forecast = forecast
        self.allocation = allocation
        self.metrics = metrics
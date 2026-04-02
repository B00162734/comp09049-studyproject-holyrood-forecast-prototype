"""
ExperimentResults
-------

The ExperimentResults class stores the forecast, seat allocation and the metrics

"""

class ExperimentResults(object):
    def __init__(self, forecast, allocation, metrics):
        self.forecast = forecast
        self.allocation = allocation
        self.metrics = metrics
"""
ForecastEngine
--------------

The ForecastEngine class computes the average vote share for each party and in future
versions will also use the ML model to compute the vote share forecast for each party.

"""

import pandas as pd

class ForecastEngine(object):
    def generate(self, data, cfg):
        #   if the baseline model is set in the configuration then the column headers (party names) for each party are used to identify the vote shares in the csv file and used to calculate the mean
        if cfg.name == "baseline":
            party_cols = ['SNP', 'Con', 'Lab', 'Green', 'Lib Dem', 'Alba', 'UKIP', 'Ref UK', 'SSP'] #    Party names
            data[party_cols] = data[party_cols].apply(pd.to_numeric, errors='coerce')   #   vote shares identified and read, converted to numeric, errors='coerce'used for error handling to swap invalad characters in the csv to 'NaN'
            #   return the calculated mean
            return data[party_cols].mean()
        else:
            raise NotImplementedError("ML model not yet implemented")   #   not yet implemented
            
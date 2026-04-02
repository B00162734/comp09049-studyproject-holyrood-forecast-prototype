"""
ForecastEngine
--------------
"""

import pandas as pd

class ForecastEngine(object):
    def generate(self, data, cfg):
        if cfg.name == "baseline":
            party_cols = ['SNP', 'Con', 'Lab', 'Green', 'Lib Dem', 'Alba', 'UKIP', 'Ref UK', 'SSP']
            data[party_cols] = data[party_cols].apply(pd.to_numeric, errors='coerce')
            return data[party_cols].mean()
        else:
            raise NotImplementedError("ML model not yet implemented")
            
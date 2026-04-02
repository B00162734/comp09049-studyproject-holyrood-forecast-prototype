"""
Test for ForecastEngine
-----------------------
"""

from src.engine import ForecastEngine
from src.config import ForecastConfig
from src.data_source import DataSource
from pathlib import Path

def test_forecast_engine():
    engine = ForecastEngine()
    cfg = ForecastConfig("baseline", {})
    data = DataSource("polls", Path("/workspaces/comp09049-studyproject-holyrood-forecast-prototype/data/processed/polling_data_processed(Sheet2).csv"), "csv").load()

    result = engine.generate(data, cfg)

    parties = ['SNP', 'Con', 'Lab', 'Green', 'Lib Dem', 'Alba', 'UKIP', 'Ref UK', 'SSP']
    for party in parties:
        assert party in result.index
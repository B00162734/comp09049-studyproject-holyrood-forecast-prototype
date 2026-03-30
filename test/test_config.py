"""
Test for ForecastConfig
--------------

"""
from src.config import ForecastConfig



def test_config():
    config = ForecastConfig("baseline", {"n_polls":5})
    assert config.name == "baseline"
    assert config.model_params == {"n_polls":5}

"""
Test for ExperimentResults
--------------------------
"""

from src.results import ExperimentResults

def test_experiment_results():
    results = ExperimentResults({'SNP: 0.40,'}, allocation={'SNP:4'}, metrics={'mae': 0.05})

    assert results.forecast
    assert results.allocation
    assert results.metrics
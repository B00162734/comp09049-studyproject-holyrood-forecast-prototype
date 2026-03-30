"""
Test for SeatAllocator
----------------------
"""

from src.allocator import SeatAllocator

def test_allocate_dhondt():
    allocator = SeatAllocator()
    forecast = ({'SNP':40, 'Con':24, 'Lab':18, 'Green':8, 'Lib Dem':5, 'Alba':0, 'UKIP':0, 'Ref UK':0, 'SSP':0 })
    result = allocator.allocate_dhondt(forecast, 7)
    assert result['SNP'] == 4
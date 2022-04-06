import pytest
@pytest .mark.parametrize("number, result", [(1, 10), (2, 20), (3, 30) ])
def test_calculation(number, result):
    assert 10*number == result
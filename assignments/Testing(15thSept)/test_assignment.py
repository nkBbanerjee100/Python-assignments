#test the conditions for factorial, prime number and area of circle with passign wrong paramters as 0
import pytest
from programms import fact,prime,area
import math
def test_fact_valid():
    assert fact(4)==24
    with pytest.raises(ValueError) as e:
        fact(0)
    assert "1" in str(e.value)

def test_prime_valid():
    assert prime(31) == True
    assert prime(17) == True
    with pytest.raises(ValueError) as e:
        prime(0)
    assert "please define a number starting from 2" in str(e.value)

def test_area_valid():
    assert math.isclose(area(4), math.pi * 16)
    with pytest.raises(ValueError) as e:
        area(0)
    assert "please define a number starting from 1" in str(e.value)
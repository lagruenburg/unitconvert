import pytest

from unitconvert.distance import miles_to_kilometers

def test_mi_to_km():
    
    # make sure that zero miles is zero kilometers
    assert miles_to_kilometers(0) == 0
    
    # check that 3 miles is 4.828032 kilometers
    assert round(miles_to_kilometers(3),1) == 4.8
    
    with pytest.raises(TypeError):
        miles_to_kilometers(1, 2)

from unitconvert.distance import kilometers_to_miles

def test_km_to_mi():
    
    # make sure zero kilometers is zero miles
    assert kilometers_to_miles(0) == 0
    
    # check that 3 kilometers is 1.86411357671
    assert round(kilometers_to_miles(3),1) == 1.9
    
    with pytest.raises(TypeError):
        kilometers_to_miles(1,2)

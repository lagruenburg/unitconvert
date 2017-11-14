import pytest

from unitconvert.temperature import fahrenheit_to_celsius

def test_F_to_C():
    
    # make sure that 32 Fahrenheit is 0 Celsius
    assert fahrenheit_to_celsius(32) == 0
    
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(1, 2)

from unitconvert.temperature import celsius_to_fahrenheit

def test_C_to_F():
    
    # check that 0 Celsius is 32 Fahrenheit
    assert round(celsius_to_fahrenheit(0),1) == 32
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(1,2)
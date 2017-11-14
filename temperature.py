"""
A python module that converts between celsius and fahrenheit
"""


def fahrenheit_to_celsius(Temperature_F):
    """Converts from fahrenheit to celsius
       
    -----
    PARAMETERS
    -----
       
    Temperature_F : float
        A single number, a temperature in degrees fahrenheit
           
    -----
    RETURNS
    -----
       
    Temperature in celsius : float
       
    """
    
    #conversion
    
    return (Temperature_F - 32)*(5/9)
    
    
def celsius_to_fahrenheit(Temperature_C):
    """Converts from celsius to fahrenheit
       
    -----
    PARAMETERS
    -----
       
    Temperature_C : float
        A single number, a temperature in degrees celsius
           
    -----
    RETURNS
    -----
       
    Temperature in fahrenheit : float
       
    """
    
    #conversion
    
    return (Temperature_C * (9/5))+32


"""
A python module that converts between miles and kilometers
"""


def miles_to_kilometers(Miles):
    """Converts from miles to kilometers
       
    -----
    PARAMETERS
    -----
       
    Miles : float
        A single number, a distance in miles
           
    -----
    RETURNS
    -----
       
    Distance in kilometers : float
       
    """
    
    #conversion
    
    return Miles*1.609
    
    
def kilometers_to_miles(Kilometers):
    """Converts from kilometers to miles
       
    -----
    PARAMETERS
    -----
       
    Kilometers : float
        A single number, a distance in kilometers
           
    -----
    RETURNS
    -----
       
    Distance in miles : float
       
    """
    
    #conversion
    
    return Kilometers/1.609


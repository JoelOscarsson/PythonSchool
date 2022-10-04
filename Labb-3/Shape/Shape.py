#TODO Skapa en parent klass shape
#TODO Skapa x_pos och y_pos koordinaterna som en int
#TODO Lägg in property för att utvidja funktioner och skrivskydda grundkoden

from __future__ import annotations

class Shape():

    def __init__(self, x_pos: (int | float), y_pos: (int | float)):
        self.x_pos = X
        self.y_pos = Y

        @property
        """Read Only"""
        def X(self):
            return self._X

        @X.setter
        def X(self, value: (int | float)):
            return self._X

        @property # För Y
        """Read Only"""
        def Y(self):
            return self._Y

        @Y.setter
        def Y(self, value1: int):
            return self._Y
            
    #TODO: göra raiseError

# Read and write properties for decorators
# Getter and setters for input value 

@property
"""Read and write for X"""
def X(self):
    return self._X

@X.setter
def X(self, value: (int | float)):
    #must be a number:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Your input must be a number, not {type(value)}")
    
    #Round to 1 decimal
    self._value = round(value, 1)
----------------------------------------------
@property
def X(self):
"""Read and write for Y"""
    return self._Y

@Y.setter
def Y(self, value: (int | float)):
    #must be a number:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Your input must be a number, not {type(value)}")
    
    #Round to 1 decimal
    self._value = round(value, 1)




        #TODO: Jag vill inte ha str
        #TODO: Jag vill inte ha någon inte skriver in ett värde
        #TODO: Jag vill inte ha 
        #TODO: Jag vill välja mellan rektangel, cirkel, cirkel2

#TODO Skapa en parent klass shape
#TODO Skapa x_pos och y_pos koordinaterna som en int
#TODO Lägg in property för att utvidja funktioner och skrivskydda grundkoden

from __future__ import annotations

class shape: # Ska göra stor bokstav

    def __init__(self, x_pos: (int | float), y_pos: (int | float)):
        print("__init__")
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        #TODO: göra raiseError

        # Read and write properties for decorators
        # Getter and setters for input value 

    @property
    def x_pos(self):
        return self._x_pos

    @x_pos.setter
    def x_pos(self, value: (int | float)):
        #must be a number:
        print("x_pos.setter")
        if not isinstance(value, (int, float)):
            raise TypeError(f"y_pos input must be a number, not {type(value)}")
        
        #Round to 1 decimal
        self._x_pos = round(value, 1)


    @property
    def y_pos(self):
    #Read and write for y_pos
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value: (int | float)):
        #must be a number:
        print("y_pos.setter")
        if not isinstance(value, (int, float)):
            raise TypeError(f"y_pos input must be a number, not {type(value)}")
        
        #Round to 1 decimal
        self._y_pos = round(value, 1)

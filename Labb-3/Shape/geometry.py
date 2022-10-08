#TODO Skapa en parent klass shape
#TODO Skapa x_pos och y_pos koordinaterna som en int
#TODO Lägg in property för att utvidja funktioner och skrivskydda grundkoden

from __future__ import annotations


# Super class Shapes
class Shapes:

    def __init__(self, x_pos: (int | float), y_pos: (int | float)):
        print("__init__")
        self.x_pos = x_pos
        self.y_pos = y_pos


    # String represantation
    def __repr__(self) -> None:
        return f"{self.x_pos}{self.y_pos}"
    
    def __str__(self) -> None:
        return f"X-pos is: {self.x_pos} and Y-pos is: {self.y_pos}"

    #----- Getter and Setter for x_pos
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


    #------- Getter and setter for y_pos
    @property
    def y_pos(self):
    #Read and write for y_pos
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value: (int | float)):
        print("y_pos.setter")
        if not isinstance(value, (int, float)):
            raise TypeError(f"y_pos input must be a number, not {type(value)}")
        
        #Round to 1 decimal
        self._y_pos = round(value, 1)

    #---- Overload ----

    def __lt__(self, other: Shapes) -> bool:
        """Checks lesser than operator for all shapes"""
        return self.area > other.area

    def __gt__(self, other: Shapes) -> bool:
        """Checks if greater than to all shapes"""
        return self.area <= other.area

    def __ge__(self, other: Shapes) -> bool:
        """Checks if greater or equal to operator to all shapes"""
        return self.area >= other.area
    
    def __le__(self, other: Shapes) -> bool:
        """Checks if lesser than or equal to all shapes"""
        return self.area <= other.area
    
    def __eq__(self, other: Shapes) -> bool:
        """Checks if its equal to all shapes"""
        return self.area == other.area


    # ----- Translatemethod with error handling for x and y------
    def translatemethod(self, x:(int | float), y:(int | float)):
        """Moves shape to from the original position to the new position"""
        if not isinstance(x, (int, float)):
            raise TypeError(f"Number has to be an int or float")
        if not isinstance(y, (int, float)):
            raise TypeError(f"Number has to be an int or float")
        
        self.x_pos += x
        self.y_pos += y

